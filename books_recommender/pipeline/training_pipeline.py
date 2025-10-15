from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.config.configuration import AppConfiguration

class TrainingPipeline:
    def __init__(self):
        self.app_config = AppConfiguration()
        self.data_ingestion = DataIngestion()

    def start_training_pipeline(self):
        self.data_ingestion.initiate_data_ingestion()