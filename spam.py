from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# ── Load vectorizer (shared across all models) ────────────────────────────────
vectorizer = joblib.load('sms_spam_vectorizer.pkl')

# ── Load all four trained models ──────────────────────────────────────────────
try:
    lr_model       = joblib.load('sms_spam_logistic_model.pkl')
    gb_model       = joblib.load('sms_spam_gradient_model.pkl')
    rf_model       = joblib.load('sms_spam_random_forest_model.pkl')
    ensemble_model = joblib.load('sms_spam_model.pkl')
    print("✅ All models loaded successfully.")
except Exception as e:
    print(f"❌ Error loading models: {e}")

# ── Model registry ────────────────────────────────────────────────────────────
MODEL_MAP = {
    "lr":       (lr_model,       "Logistic Regression"),
    "gb":       (gb_model,       "Gradient Boosting"),
    "rf":       (rf_model,       "Random Forest"),
    "ensemble": (ensemble_model, "Ensemble Model"),
}

# ── Route ─────────────────────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction        = None
    selected_model_name = None
    selected_model_key  = 'lr'   # default on GET

    if request.method == 'POST':
        user_input   = request.form.get('message', '').strip()
        model_choice = request.form.get('model', 'lr')

        selected_model_key = model_choice  # keep dropdown on same option after submit

        if not user_input:
            return render_template('sms_spam.html',
                                   prediction=None,
                                   selected_model_name=None,
                                   selected_model_key=selected_model_key)

        # Pick model
        model, model_name = MODEL_MAP.get(model_choice, MODEL_MAP['lr'])
        selected_model_name = model_name

        # Vectorize and predict
        vectorized = vectorizer.transform([user_input])
        result     = model.predict(vectorized)[0]
        prediction = 'Spam' if result == 1 else 'Ham'

    return render_template('sms_spam.html',
                           prediction=prediction,
                           selected_model_name=selected_model_name,
                           selected_model_key=selected_model_key)

if __name__ == '__main__':
    app.run(debug=True)