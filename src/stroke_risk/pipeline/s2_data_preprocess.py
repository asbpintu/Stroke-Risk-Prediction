from stroke_risk.config.configuration import ConfigurationManager
from stroke_risk.components.c2_data_preprocess import DataPreprocess

from stroke_risk import logger


stage_name = 'Data PreProcess'

class DataPreprocessPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_preprocess_config = config.get_data_preprocess_config()
        data_preprocess = DataPreprocess(config=data_preprocess_config)
        data_preprocess.preprocess()



if __name__ == '__main__':
    try:
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = DataPreprocessPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e