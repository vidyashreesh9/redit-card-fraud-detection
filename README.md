***💳 Credit Card Fraud Detection - Full Stack Application***

This project is a full-stack web application that uses a machine learning model to detect fraudulent credit card transactions in real-time.

It consists of:

Frontend: A responsive React and TypeScript application for user input.

Backend: A FastAPI (Python) server that serves a pre-trained scikit-learn model.

✨ User Interface & Features

The user interface is a clean, single-page application designed for ease of use. It allows a user (such as a data analyst or bank representative) to manually enter transaction data and get an immediate fraud assessment.

1. Transaction Input Form

The main page presents a comprehensive form with 30 required input fields, which directly correspond to the features in the training dataset.

Layout: The form uses a responsive CSS grid that neatly arranges all 30 fields, adapting to different screen sizes.

Fields:

Time: The elapsed time since the first transaction in the dataset.

Amount: The monetary value of the transaction.

V1 - V28: Anonymized PCA features from the original dataset.

2. Dynamic User Feedback

The UI provides instant and clear feedback to the user throughout the prediction process.

Loading State: When the user clicks the "Check Transaction" button, the button becomes disabled and its text changes to "Checking...". This prevents duplicate submissions and informs the user that a request is in progress.

Result: Not Fraudulent (Success)
If the model predicts the transaction is legitimate, a green-themed result box appears.

Style: The box has a light green background and a solid green left border (.not-fraud).

Message: Displays the text "Not Fraudulent" in a bold, green font.

Details: Shows the precise probability of fraud (e.g., "Probability of Fraud: 0.15%").

Result: Fraudulent (Warning)
If the model flags the transaction as suspicious, a red-themed warning box appears.

Style: The box has a light red background and a solid red left border (.fraud).

Message: Displays the text "Fraudulent" in a bold, red font.

Details: Shows the high probability of fraud (e.g., "Probability of Fraud: 85.60%").

Error Handling
If the frontend fails to communicate with the backend API (e.g., the server isn't running), a distinct error message appears, informing the user that an error occurred and suggesting they check the backend.

🏗️ System Architecture

The application operates with a simple and efficient client-server architecture:

User Input: The user fills out the 30 transaction fields in the React Frontend.

API Request: On submit, Axios sends the form data as a JSON payload to the http://localhost:8000/predict endpoint.

Backend Processing: The FastAPI Backend receives the JSON, validates it using a Pydantic Transaction model, and converts it to a Pandas DataFrame.

Data Preprocessing: The backend loads the saved scaler.joblib and uses it to scale the Time and Amount features, exactly matching the preprocessing done during training.

Prediction: The preprocessed DataFrame is fed into the loaded fraud_detection_model.joblib (a LogisticRegression model). The model predicts the class (0 or 1) and the fraud probability.

API Response: The backend returns a JSON response to the client, e.g., {"is_fraud": 1, "fraud_probability": "90.00%", "prediction": "Fraudulent"}.

UI Display: The React Frontend receives the JSON response, updates its state, and conditionally renders the appropriate result box (green for "Not Fraudulent", red for "Fraudulent").

🛠️ Tech Stack

Backend (backend/)

Python: Core programming language.

FastAPI: High-performance web framework for building the API.

Uvicorn: ASGI server to run the FastAPI application.

Scikit-learn: Used to train the LogisticRegression model and the StandardScaler.

Pandas: For data preprocessing and DataFrame creation.

Joblib: For saving and loading the trained model (.joblib) and scaler.

Frontend (frontend/)

React: JavaScript library for building the user interface.

TypeScript: Adds static typing to JavaScript for more robust code.

Axios: Promise-based HTTP client for making API requests.

CSS: Custom styling for the form, grid layout, and dynamic result boxes.

🚀 Setup and Usage

Follow these steps to set up and run the project on your local machine.

Prerequisites

Node.js and npm: Required for the frontend. Download from https://nodejs.org/

Python (3.7+): Required for the backend. Download from https://www.python.org/

Step 1: Download the Dataset

This project requires the "Credit Card Fraud Detection" dataset from Kaggle.

Download the file: Go to https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Extract and place the file: Unzip the downloaded file to get creditcard.csv.

Move the file: Place the creditcard.csv file inside the backend directory of this project.

The final path should be: backend/creditcard.csv.

Step 2: Set Up and Run the Backend

The backend server handles model training and real-time predictions.

Navigate to the backend directory:

cd backend


Create a virtual environment (recommended):

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate


Install Python dependencies:

pip install -r requirements.txt 


Train the machine learning model:
Run the training script. This will use creditcard.csv to train the model and save fraud_detection_model.joblib and scaler.joblib inside the backend folder.

python model.py


You should see a classification report printed to the console upon completion.

Start the backend server:
This will run the API server on http://localhost:8000.

uvicorn main:app --reload


Keep this terminal open.

Step 3: Set Up and Run the Frontend

The frontend is the React application that provides the user interface.

Open a new terminal.

Navigate to the frontend directory:

cd frontend


Install JavaScript dependencies:

npm install


Start the frontend development server:
This will open the application in your web browser at http://localhost:3000.

npm start


Step 4: Use the Application

With both the backend and frontend servers running, your browser should open to http://localhost:3000.

The page will display the form with 30 fields.

Fill in the transaction data. You can copy a row from the creditcard.csv file to use as sample data (remember to exclude the Class column).

Click "Check Transaction".

The result ("Fraudulent" or "Not Fraudulent") will be displayed below the form.
