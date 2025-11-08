import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

// This defines the structure of the prediction response from the API
interface PredictionResponse {
  prediction: string;
  is_fraud: number;
  fraud_probability: string;
}

function App() {
  // State to hold the form data
  const [formData, setFormData] = useState({
    Time: '', V1: '', V2: '', V3: '', V4: '', V5: '', V6: '', V7: '', V8: '', V9: '',
    V10: '', V11: '', V12: '', V13: '', V14: '', V15: '', V16: '', V17: '', V18: '',
    V19: '', V20: '', V21: '', V22: '', V23: '', V24: '', V25: '', V26: '', V27: '',
    V28: '', Amount: ''
  });

  // State for the prediction result, loading status, and errors
  const [prediction, setPrediction] = useState<PredictionResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Handle changes in form inputs
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // Convert form data from strings to numbers
      const transactionData = Object.fromEntries(
        Object.entries(formData).map(([key, value]) => [key, Number(value)])
      );

      // Send data to the backend API
      const response = await axios.post('http://localhost:8000/predict', transactionData);
      setPrediction(response.data);

    } catch (err) {
      setError('An error occurred while making the prediction. Please ensure the backend is running and the input values are correct.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };
  
  // Create a list of the 'V' feature names for easier rendering
  const vFeatures = Array.from({ length: 28 }, (_, i) => `V${i + 1}`);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Credit Card Fraud Detection</h1>
        <p>Enter transaction details to check for fraud.</p>
      </header>
      <main>
        <form onSubmit={handleSubmit} className="transaction-form">
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="Time">Time</label>
              <input type="number" step="any" name="Time" placeholder="Time" onChange={handleChange} value={formData.Time} required />
            </div>
            <div className="form-group">
              <label htmlFor="Amount">Amount</label>
              <input type="number" step="any" name="Amount" placeholder="Amount" onChange={handleChange} value={formData.Amount} required />
            </div>
            {vFeatures.map(feature => (
              <div className="form-group" key={feature}>
                <label htmlFor={feature}>{feature}</label>
                <input type="number" step="any" name={feature} placeholder={feature} onChange={handleChange} value={formData[feature as keyof typeof formData]} required />
              </div>
            ))}
          </div>
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Checking...' : 'Check Transaction'}
          </button>
        </form>

        {error && <div className="error-message">{error}</div>}

        {prediction && (
          <div className={`result-section ${prediction.is_fraud === 1 ? 'fraud' : 'not-fraud'}`}>
            <h2>Prediction Result</h2>
            <p className="result-text">{prediction.prediction}</p>
            <p>Probability of Fraud: {prediction.fraud_probability}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
