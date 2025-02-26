from Mlproject.components.data_transformation import DataTransformation
from Mlproject.config.configuration import ConfigurationManager
from Mlproject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(": ")[1].strip() 

            if status == "True":
                config = ConfigurationManager()  
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)  # Removed extra parentheses
                data_transformation.train_test_spliting()

            else:
                raise Exception("your data schema is not valid")
           
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e