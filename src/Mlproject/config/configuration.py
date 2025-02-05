from Mlproject.entity.config_entity import *
from Mlproject.utils.common import read_yaml, create_directories
from Mlproject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
import logging
from Mlproject.constants import *

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

class ConfigurationManager:

    def __init__(
        self, 
        config_filepath= CONFIG_FILE_PATH,
        params_filepath= PARAMS_FILE_PATH,
        schema_filepath= SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        self.artifacts_root = Path(self.config.get('artifacts_root', 'artifacts'))

        create_directories([self.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    

    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.get('data_validation', {})
        schema = self.schema.get('Columns', {})
        logging.info(f"Loaded schema: {schema}")
        
        # Use default values if keys are missing
        root_dir = Path(config.get('root_dir', self.artifacts_root / 'data_validation'))
        status_file = config.get('STATUS_FILE', 'status.txt')
        unzip_data_dir = Path(config.get('unzip_data_dir', self.artifacts_root / 'data'))

        create_directories([root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=root_dir,
            STATUS_FILE=status_file,
            unzip_data_dir=unzip_data_dir,
            all_schema=schema,
        )

        logging.info(f"Data Validation Config: {data_validation_config}")
        return data_validation_config   


    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            config = self.config.data_transformation
            logging.info(f"Data transformation config: {config}")
        except Exception as e:
            logging.error(f"Error reading data_transformation config: {str(e)}")
            logging.error(f"Available config keys: {self.config.keys()}")
            raise

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )

        return data_transformation_config
    



    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path, 
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio, 
            target_column=schema.name
        )
        
        return model_trainer_config 