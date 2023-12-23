from stroke_risk.pipeline.s1_data_ingestion import DataIngestionPipeline
from stroke_risk.pipeline.s2_data_preprocess import DataPreprocessPipeline
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



logger.info(f'\n\n\n===================== PROGRAMME COMPLETED =====================\n\n\n')