from src.components.stage_00_data_ingestion import DataIngestionGDrive
from src.config.configuration import AppConfiguration

if __name__ == "__main__":
    config = AppConfiguration()
    ingestion = DataIngestionGDrive(config)
    ingestion.initiate_data_ingestion()
