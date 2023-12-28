from stroke_risk.components.c5_model_training import ModelTraining
from stroke_risk.config.configuration import ConfigurationManager

from stroke_risk import logger


stage_name = 'Model Training'


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer_config = ModelTraining(config=model_trainer_config)
        model_trainer_config.training()



if __name__ == '__main__':
    try:
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = ModelTrainingPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e
