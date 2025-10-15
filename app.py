import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


class Recommendation:
    def __init__(self,app_config = AppConfiguration()):
        try:
            self.recommendation_config= app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e


    def fetch_poster(self,suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
            final_rating =  pickle.load(open(self.recommendation_config.final_rating_serialized_objects,'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]: 
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url
        
        except Exception as e:
            raise AppException(e, sys) from e
        


    def recommend_book(self, book_name, n_recommendations=5):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path,'rb'))
            book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            
            distance, suggestion = model.kneighbors(
                book_pivot.iloc[book_id,:].values.reshape(1,-1), 
                n_neighbors=n_recommendations+1
            )

            poster_url = self.fetch_poster(suggestion)
            
            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)
            
            # remove the first book itself from the list
            return books_list[1:], poster_url[1:]   
        except Exception as e:
            raise AppException(e, sys) from e



    def train_engine(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training Completed!")
            logging.info(f"Recommended successfully!")
        except Exception as e:
            raise AppException(e, sys) from e

    
    def recommendations_engine(self, selected_books, n_recommendations):
        try:
            recommended_books, poster_url = self.recommend_book(selected_books, n_recommendations)
        
            for i in range(n_recommendations):
                st.image(poster_url[i], width=150)  # set width to keep images uniform
                st.subheader(recommended_books[i])  # book name as subheader
                st.markdown("<br>", unsafe_allow_html=True)  # adds some spacing

        except Exception as e:
            raise AppException(e, sys) from e







if __name__ == "__main__":
    st.header('Books Recommendations')
    st.text("This is a collaborative filtering based recommendation system!")

    obj = Recommendation()

    if st.button('Train Recommender System'):
        obj.train_engine()

    book_names = pickle.load(open(os.path.join('artifacts/serialized_objects','book_names.pkl') ,'rb'))
    selected_books = st.selectbox(
        "Type or select a book from the dropdown",
        book_names)
    num_recommendations = st.number_input(
    "Select number of recommendations to show", 
    min_value=1, max_value=20, value=5, step=1)
    
    if st.button('Show Recommendations'):
        obj.recommendations_engine(selected_books, num_recommendations)
