# Credit Card Fraud Detection

This project uses a machine learning model to detect fraudulent credit card transactions.

## Project Structure

- `backend/`: Contains the Python FastAPI server and the machine learning model.
- `frontend/`: Contains the React-based user interface.

## Setup and Usage

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- **Node.js and npm:** Required for the frontend. Download from [https://nodejs.org/](https://nodejs.org/)
- **Python:** Required for the backend. Download from [https://www.python.org/](https://www.python.org/)

---

### Step 1: Download the Dataset

This project requires the "Credit Card Fraud Detection" dataset from Kaggle.

1.  **Download the file:** Go to [https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
2.  **Extract and place the file:** Unzip the downloaded file and you will find `creditcard.csv`.
3.  **Move the file:** Place the `creditcard.csv` file inside the `backend` directory of this project.

The final path should be: `credit-card-fraud-detection/backend/creditcard.csv`.

---

### Step 2: Set Up and Run the Backend

The backend is a Python server that handles the machine learning predictions.

1.  **Navigate to the backend directory:**
    ```bash
    cd credit-card-fraud-detection/backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    Activate it:
    -   **Windows:** `venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Train the machine learning model:**
    Run the training script. This will use `creditcard.csv` to train the model and save it as `fraud_detection_model.joblib`.
    ```bash
    python model.py
    ```

5.  **Start the backend server:**
    This will run the API server on `http://localhost:8000`.
    ```bash
    uvicorn main:app --reload
    ```
    Keep this terminal open.

---

### Step 3: Set Up and Run the Frontend

The frontend is a React application that provides the user interface.

1.  **Open a new terminal.**

2.  **Navigate to the frontend directory:**
    ```bash
    cd credit-card-fraud-detection/frontend
    ```

3.  **Install JavaScript dependencies:**
    ```bash
    npm install
    ```

4.  **Start the frontend development server:**
    This will open the application in your web browser at `http://localhost:3000`.
    ```bash
    npm start
    ```

---

### Step 4: Use the Application

1.  With both the backend and frontend servers running, your browser should open to `http://localhost:3000`.
2.  The page will display a form with fields for `Time`, `Amount`, and 28 `V` features.
3.  Fill in the transaction data. You can use a row from the `creditcard.csv` file as sample data.
4.  Click **"Check Transaction"**.
5.  The result ("Fraudulent" or "Not Fraudulent") will be displayed below the form.
# redit-card-fraud-detection# redit-card-fraud-detection
