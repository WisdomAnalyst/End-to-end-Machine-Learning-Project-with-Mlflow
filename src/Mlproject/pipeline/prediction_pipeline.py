import joblib
import numpy as np
import os

class PredictionPipeline:
    def __init__(self, model_path="Mlproject/artifacts/model.joblib"):
        """
        Initialize the pipeline and load the trained model.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}. Train the model first.")

        # Load model using joblib
        self.model = joblib.load(model_path)

    def predict(self, data):
        """
        Predict the quality of wine based on input features.

        :param data: np.array with shape (1, 11) (one sample, 11 features)
        :return: np.array with predicted quality score
        """
        if not isinstance(data, np.ndarray):
            raise ValueError("Input data must be a NumPy array.")
        
        if data.shape[1] != 11:
            raise ValueError(f"Expected input shape (1, 11), but got {data.shape}")

        prediction = self.model.predict(data)
        return prediction
