from Mlproject.components.data_ingestion import DataIngestion
from Mlproject.config.configuration import ConfigurationManager
from Mlproject import logger


STAGE_NAME = "Data Ingestion stage"


class DataingestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):  # This should be indented to be part of the class
        config = ConfigurationManager() 
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataingestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e