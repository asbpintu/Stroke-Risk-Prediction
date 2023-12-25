from stroke_risk.constants import *
from stroke_risk.utils.common import read_yaml, create_directories

from stroke_risk.entity.config_entity import DataIngestionConfig
from stroke_risk.entity.config_entity import DataPreprocessConfig
from stroke_risk.entity.config_entity import DataValidationConfig



class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
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
    
    def get_data_preprocess_config(self) -> DataPreprocessConfig:
        config = self.config.data_preprocess

        create_directories([config.root_dir])

        data_preprocess_config = DataPreprocessConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir,
            dataset_name=config.dataset_name,
            save_data_file=config.save_data_file 
        )

        return data_preprocess_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            data_dir = config.data_dir,
            all_schema=schema,
        )

        return data_validation_config