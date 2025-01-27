from Mlproject.components.model_trainer import ModelTrainer
from Mlproject.config.configuration import ConfigurationManager
from Mlproject import logger


STAGE_NAME = "Data Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()  
    model_trainer_config = ModelTrainer(config=model_trainer_config)
    model_trainer_config.train()    