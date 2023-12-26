from stroke_risk.config.configuration import ConfigurationManager
from stroke_risk.components.c4_data_transformation import DataTransformation

from stroke_risk import logger


stage_name = 'Data Transformation'


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.encoding()
        data_transformation.train_test_spliting()




if __name__ == '__main__':
    try:
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = DataTransformationPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e
