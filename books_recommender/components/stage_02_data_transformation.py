import os 
import sys 
import pickle
import pandas as pd
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException

class DataTransformation:
    def __init__(self, app_config=AppConfiguration())-> None:
        try:
            logging.info(f"{'='*20} Data Transformation log : {'='*20}")
            if app_config is None:
                app_config = AppConfiguration()
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_transformer_object(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)
            book_pivot = df.pivot_table(columns='user_id', index='title', values='rating')
            book_pivot.fillna(0, inplace=True)

            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(book_pivot, open(os.path.join(self.data_transformation_config.transformed_data_dir,"transformed_data.pkl"),'wb'))
            logging.info(f"Saved pivot table data to {self.data_transformation_config.transformed_data_dir}")

            book_names = book_pivot.index

            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_validation_config.serialized_objects_dir,"book_names.pkl"),'wb'))
            logging.info(f"Saved book names serialization object to {self.data_validation_config.serialized_objects_dir}")

            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(book_pivot, open(os.path.join(self.data_validation_config.serialized_objects_dir,"book_pivot.pkl"),'wb'))
            logging.info(f"Saved book pivot serialization object to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise AppException(e, sys) from e


    def initiate_data_transformation(self):
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
            self.get_data_transformer_object()
            logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e        

