import os  
import pandas as pd  
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  
from urllib.parse import urlparse  
import mlflow  
import mlflow.sklearn  
import numpy as np  
import joblib 
from typing import Any 
from Mlproject.entity.config_entity import ModelEvaluationConfig
from Mlproject.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):  
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))  
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)  
        model = joblib.load(self.config.model_path)  

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)  
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme  

        with mlflow.start_run(run_name="ElasticNet_Wine_Quality_Model"):
            # Add tags
            mlflow.set_tag("model_type", "ElasticNet")
            mlflow.set_tag("data_source", "Wine Quality Dataset")
            mlflow.set_tag("experiment_description", "Baseline model with default parameters")

            # Log parameters
            mlflow.log_params({
                "alpha": self.config.all_params["alpha"],
                "l1_ratio": self.config.all_params["l1_ratio"],
                "data_version": "v1.0",
                "model_version": "ElasticNet_v1"
            })
            
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)  

            # Log metrics to MLflow
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Log model to MLflow
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model, 
                    "model", 
                    registered_model_name="ElasticModel"  
                )
            else:
                mlflow.sklearn.log_model(model, "model")