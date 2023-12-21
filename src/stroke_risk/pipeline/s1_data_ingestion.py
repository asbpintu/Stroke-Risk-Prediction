from stroke_risk.config.configuration import ConfigurationManager
from stroke_risk.components.c1_data_ingestion import DataIngestion
from stroke_risk import logger





stage_name = 'Data Ingestion'


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass


    def main(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f'\n\n\n===================== PROGRAMME STARTED =====================\n\n\n')
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Started) ********\n\n')
        cal = DataIngestionPipeline()
        cal.main()
        logger.info(f'\n\n******** Stage :  {stage_name} --> (Completed) ********\n\n')
    except Exception as e:
        logger.exception(e)
        raise e