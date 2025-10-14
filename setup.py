from setuptools import setup, find_packages

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME = "Book-Recommender-System-using-Collaborative-Filtering-and-Streamlit"
AUTHOR_USER_NAME = "sameer-at-git"    
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A book recommender system using collaborative filtering and Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https:github.com/sameer-at-git/Book-Recommender-System-using-Collaborative-Filtering-and-Streamlit",
    author_email="mdsameersayed0@gmail.com",
    packages=find_packages(),
    license='MIT',
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS

)