from Mlproject import logger
from Mlproject.pipeline.stage_01_dataIngestion import DataingestionTrainingPipeline
from Mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Mlproject.pipeline.stage_03_dataTransformation import DataTransformationTrainingPipeline
from Mlproject.pipeline.stage_04_modeltrainer import ModelTrainerTrainingPipeline
from Mlproject.pipeline.stage_05_modelevaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_Ingestion= DataingestionTrainingPipeline()
    data_Ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_Ingestion= DataValidationTrainingPipeline()
    data_Ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Transformation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e    


STAGE_NAME = "model evaluation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
