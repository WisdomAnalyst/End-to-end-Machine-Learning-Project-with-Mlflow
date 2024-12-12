from Mlproject import logger
from Mlproject.pipeline.stage_01_dataIngestion import DataingestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_Ingestion= DataingestionTrainingPipeline()
    data_Ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e