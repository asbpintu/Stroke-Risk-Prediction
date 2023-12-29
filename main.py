from stroke_risk.pipeline.s1_data_ingestion import DataIngestionPipeline
from stroke_risk.pipeline.s2_data_preprocess import DataPreprocessPipeline
from stroke_risk.pipeline.s3_data_validation import DataValiadtionPipeline
from stroke_risk.pipeline.s4_data_transformation import DataTransformationPipeline
from stroke_risk.pipeline.s5_model_training import ModelTrainingPipeline
from stroke_risk.pipeline.s6_model_evaluation import ModelEvaluationPipeline
from stroke_risk import logger




logger.info(f'\n\n\n===================== PROGRAMME STARTED =====================\n\n\n')



stage_name = 'Data Ingestion'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = DataIngestionPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e


stage_name = 'Data PreProcess'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = DataPreprocessPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e


stage_name = 'Data Validation'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = DataValiadtionPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e



stage_name = 'Data Transformation'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = DataTransformationPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e



stage_name = 'Model Training'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = ModelTrainingPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Model Evaluation'

try:
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
    cal = ModelEvaluationPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e



logger.info(f'\n\n\n===================== PROGRAMME COMPLETED =====================\n\n\n')