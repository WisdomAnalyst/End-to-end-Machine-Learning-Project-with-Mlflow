import pandas as pd
import os
from Mlproject import logging
from Mlproject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            # Add debug logging
            logging.info(f"Schema content: {self.config.all_schema}")
            logging.info(f"Schema type: {type(self.config.all_schema)}")

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            logging.info(f"Data columns: {all_cols}")

            # Try different ways to access schema
            try:
                # Method 1: Direct attribute access
                all_schema = list(self.config.all_schema.COLUMNS.keys())
            except AttributeError:
                try:
                    # Method 2: Dictionary access
                    all_schema = list(self.config.all_schema['COLUMNS'].keys())
                except (KeyError, TypeError):
                    # Method 3: If schema is flat
                    all_schema = list(self.config.all_schema.keys())

            logging.info(f"Schema columns: {all_schema}")

            if not all_schema:
                logging.warning("Schema is empty. Skipping validation.")
                return True

            # Validate columns
            validation_status = True  # Start with True
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logging.warning(f"Column {col} not found in schema")

            # Write final status
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"validation status: {validation_status}")

            return validation_status
                
        except Exception as e:
            logging.error(f"Error in validate_all_columns: {str(e)}")
            logging.error(f"Schema content at error: {self.config.all_schema}")
            raise e