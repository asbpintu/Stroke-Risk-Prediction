import pandas as pd
from stroke_risk import logger

from stroke_risk.entity.config_entity import DataValidationConfig



class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"COLUMNS: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"COLUMNS: {validation_status}\n")
        except Exception as e:
            raise e
    

    def validate_all_datatypes(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema

            for col in all_cols:
                if all_schema[col] != data[col].dtype.name:
                    validation_status = False
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"{col}: {validation_status}\n")
                    
                    logger.info(f'{col} = {all_schema[col]}: {data[col].dtype.name}')
                else:
                    validation_status = True
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"{col}: {validation_status}\n")
        except Exception as e:
            raise e
    

    def check_validation(self)-> bool:
        try:
            with open(self.config.status_file, 'r') as f:
                status = [stat.strip() for stat in f.readlines()]
                f.close()

            status = {key.strip(): value.strip().lower()=='true' for key,value in [stat.split(':') for stat in status]}

            if all(status.values()):
                logger.info('All Validation Passed')
            else:
                logger.info('Validation Failed')
        except Exception as e:
            raise e