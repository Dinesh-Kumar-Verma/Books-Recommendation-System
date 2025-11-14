import os
import sys
import zipfile
import gdown
from src.logger.log import logging
from src.exception.exception_handler import AppException
from src.config.configuration import AppConfiguration


class DataIngestionGDrive:

    def __init__(self, app_config: AppConfiguration = AppConfiguration()):
        """
        Data Ingestion Initialization (Google Drive Only)

        app_config: AppConfiguration
        """
        try:
            logging.info(f"{'='*20}Data Ingestion (GDrive) log started.{'='*20}")
            self.data_ingestion_config = app_config.get_data_ingestion_config()

        except Exception as e:
            raise AppException(e, sys) from e


    def download_data(self) -> str:
        """
        Download dataset from Google Drive using gdown.
        Returns:
            str: Path to the downloaded ZIP file.
        """
        try:
            gdrive_url = self.data_ingestion_config.dataset_download_url
            download_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(download_dir, exist_ok=True)

            zip_file_path = os.path.join(download_dir, "data.zip")

            logging.info(f"Downloading dataset from Google Drive URL: {gdrive_url}")
            gdown.download(gdrive_url, zip_file_path, quiet=False, fuzzy=True)

            logging.info(f"Dataset downloaded successfully at: {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys) from e


    def extract_zip_file(self, zip_file_path: str):
        """
        Extract the ZIP file safely into the ingestion directory.
        """
        try:
            extract_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(extract_dir, exist_ok=True)

            logging.info(f"Extracting ZIP file: {zip_file_path} into {extract_dir}")

            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                for member in zip_ref.namelist():
                    member_path = os.path.join(extract_dir, member)
                    abs_target = os.path.abspath(member_path)
                    abs_extract = os.path.abspath(extract_dir)

                    # Prevent Zip Slip
                    if not abs_target.startswith(abs_extract):
                        raise AppException(
                            Exception(f"Unsafe file path detected: {member}"), sys
                        )

                zip_ref.extractall(extract_dir)

            logging.info(f"Extraction completed successfully.")

        except Exception as e:
            raise AppException(e, sys) from e


    def initiate_data_ingestion(self):
        """
        Orchestrates the Google Drive data ingestion workflow.
        """
        try:
            zip_path = self.download_data()
            self.extract_zip_file(zip_path)

            logging.info(f"{'='*20}Data Ingestion (GDrive) completed.{'='*20}\n\n")

        except Exception as e:
            raise AppException(e, sys) from e
