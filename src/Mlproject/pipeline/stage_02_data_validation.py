from Mlproject.config.configuration import ConfigurationManager
from Mlproject.components.data_validation import DataValidation
from Mlproject import logging

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
            
        except Exception as e:
            raise e
