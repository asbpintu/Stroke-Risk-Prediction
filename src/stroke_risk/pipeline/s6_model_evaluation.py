from stroke_risk.config.configuration import ConfigurationManager
from stroke_risk.components.c6_model_evaluation import ModelEvaluation

from stroke_risk import logger



stage_name = 'Model Evaluation'


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = ModelEvaluationPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e