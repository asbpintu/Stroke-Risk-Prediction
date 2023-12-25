from stroke_risk.config.configuration import ConfigurationManager
from stroke_risk.components.c3_data_validation import DataValiadtion
from stroke_risk import logger


stage_name = 'Data Validation'


class DataValiadtionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_datatypes()
        data_validation.check_validation()



if __name__ == '__main__':
    try:
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = DataValiadtionPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e