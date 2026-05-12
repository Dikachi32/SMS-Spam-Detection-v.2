# SMS Spam Detection System V2

SMS Spam Detection System V2 is an advanced Machine Learning project designed to intelligently classify SMS messages as either Spam or Ham (Not Spam) using multiple AI models.

This project is an upgraded version of the previous SMS Spam Detection System, which originally relied on only a single machine learning algorithm. In Version 2, the system was redesigned to support multiple machine learning models, enabling real-time prediction comparison, improved accuracy analysis, and better overall performance.

The system was built to demonstrate how different machine learning algorithms perform on the same SMS dataset while providing users with a clean and interactive prediction experience.

## 🎥 Watch Live Demo:
https://www.linkedin.com/posts/dikachi-baron-a4a380356_machinelearning-artificialintelligence-datascience-ugcPost-7460065266744524800-SNgx?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFiwEdoBhQHM9RGHGnevgOcCk1gtXoCOlv8

## Features

* Multi-model AI prediction system
* Real-time SMS message classification
* Spam and Ham message detection
* Performance comparison between models
* Accuracy visualization using professional graphs
* Interactive prediction workflow
* Ensemble learning integration for improved accuracy

## Machine Learning Models Used

The project integrates multiple machine learning algorithms, including:

* Logistic Regression
* Gradient Boosting
* Random Forest
* Ensemble Model

Each model independently analyzes incoming SMS messages and predicts whether the message is Spam or Ham.

## Project Workflow

The workflow of the system includes:

1. Data Collection
   SMS datasets containing spam and legitimate messages were collected for training and testing purposes.

2. Data Preprocessing
   The text data was cleaned and transformed using Natural Language Processing (NLP) techniques such as:

   * Lowercasing
   * Removing punctuation
   * Tokenization
   * Stopword removal
   * Text vectorization

3. Model Training
   Multiple machine learning models were trained using the processed SMS dataset.

4. Model Evaluation
   Each model was evaluated based on accuracy and prediction performance.

5. Real-Time Prediction
   Users can input SMS messages into the system, and the selected model predicts whether the message is Spam or Ham instantly.

6. Performance Visualization
   A professional comparison graph was created to visualize the accuracy of all machine learning models.

## Model Accuracy Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 97.6%    |
| Gradient Boosting   | 97.3%    |
| Random Forest       | 97.9%    |
| Ensemble Model      | 98.1%    |

The Ensemble Model achieved the highest overall accuracy, demonstrating the effectiveness of combining multiple algorithms for better spam detection performance.

## Live Demo Testing

During the live demonstration, both spam and non-spam messages were tested across all machine learning models.

Example Spam Message:
“Congratulations! You have won a FREE iPhone. Click the link below to claim your reward.”

All models successfully detected the message as Spam.

Example Ham Message:
“Hey Francis, are we still meeting for the machine learning project discussion by 4 PM today?”

All models correctly classified the message as Ham.

The live testing demonstrated the consistency, reliability, and effectiveness of the system in real-world SMS classification scenarios.

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Natural Language Processing (NLP)
* Machine Learning
* Ensemble Learning
* Matplotlib / Visualization Tools

## Project Goal

The primary goal of this project is to develop an intelligent SMS filtering system capable of accurately identifying spam messages while minimizing false predictions.

This project also demonstrates the practical application of:

* Machine Learning
* NLP
* Model Comparison
* Ensemble Learning
* Real-Time AI Prediction Systems

## Conclusion

SMS Spam Detection System V2 showcases the power of combining multiple machine learning algorithms to build a reliable and efficient spam classification system.

By integrating Logistic Regression, Gradient Boosting, Random Forest, and Ensemble Learning into a single platform, the project provides improved prediction accuracy, real-time performance comparison, and a more advanced AI-powered user experience.

This project represents a strong practical implementation of Machine Learning and Natural Language Processing for intelligent communication filtering systems.

Developed by Dikachi Baron.
