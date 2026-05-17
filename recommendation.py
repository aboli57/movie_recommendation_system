import streamlit as st
import pandas as pd
import pickle

# Load movie dataset and recommendation model
# movies.pkl and similarity.pkl
try:
    movies_list = pickle.load(open('movies.pkl','rb'))
    similarity = pickle.load(open('similarity.pkl','rb'))
except FileNotFoundError:
    sr.error("Model files not found. Please run the notebook 'Recommendation System.ipynb' to generate 'movies.pkl' & 'similarity.pkl'.")
    st.stop()

movies = pd.DataFrame(movies_list)

def recommend(movie):
    movies_index = movies[movies['title']==movie].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key= lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie Recoomendation System")
selected_movie_name = st.selectbox("Select a movie to get recommendations", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)