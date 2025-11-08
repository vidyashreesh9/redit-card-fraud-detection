import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_model():
    """
    This function trains a logistic regression model on the credit card fraud dataset.
    """
    # IMPORTANT: Download the dataset from Kaggle and place it in this 'backend' directory.
    # URL: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
    file_path = 'backend/creditcard.csv'

    if not os.path.exists(file_path):
        print(f"ERROR: Dataset not found at {file_path}")
        print("Please download 'creditcard.csv' from https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud and place it in the 'backend' directory.")
        return

    print("Loading dataset...")
    data = pd.read_csv(file_path)

    # Preprocessing
    # Scale 'Time' and 'Amount'
    scaler = StandardScaler()
    data['scaled_amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
    data['scaled_time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))
    data.drop(['Time', 'Amount'], axis=1, inplace=True)

    # Move 'Class' to the end
    X = data.drop('Class', axis=1)
    y = data['Class']

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Training model...")
    model = LogisticRegression(solver='liblinear', random_state=42)
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save the model and the scaler
    print("Saving model...")
    joblib.dump(model, 'backend/fraud_detection_model.joblib')
    joblib.dump(scaler, 'backend/scaler.joblib')
    print("Model training complete. Model saved to 'backend/fraud_detection_model.joblib'")

if __name__ == "__main__":
    train_model()
