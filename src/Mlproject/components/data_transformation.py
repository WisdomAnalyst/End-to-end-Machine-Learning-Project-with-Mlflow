import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from Mlproject.entity.config_entity import DataTransformationConfig
import logging

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self): 
        try:
            # Read the data
            data = pd.read_csv(self.config.data_path)

            # Split the data into training and test sets 
            train, test = train_test_split(data, test_size=0.2, random_state=42)
            
            # Save the split datasets
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            # Log the information
            logging.info("Split data into training and test sets")
            logging.info(f"Training set shape: {train.shape}")
            logging.info(f"Test set shape: {test.shape}")

            # Print shapes
            print(f"Training set shape: {train.shape}")
            print(f"Test set shape: {test.shape}")

        except Exception as e:
            logging.error(f"Error in train_test_splitting: {str(e)}")
            raise e