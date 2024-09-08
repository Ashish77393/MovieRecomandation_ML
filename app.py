from http.client import responses

import streamlit as st
import pandas as pd
import pickle
import requests



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d3f1a5b32856fd956d1fd62fc5576e51&Language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recomanded(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recomandedmovie=[]
    recomanded_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recomandedmovie.append(movies.iloc[i[0]].title)
        # fetch poster API Poster
        recomanded_movie_poster.append(fetch_poster(movie_id))
    return recomandedmovie,recomanded_movie_poster
moviedata=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(moviedata)
st.title("movie Recomanded System")
optionmovie = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values



)
import streamlit as st

# Create a sidebar navbar
st.sidebar.title("Navigation")
nav_selection = st.sidebar.radio("Go to", ["Home", "Movies", "About"])

# Display content based on navbar selection
if nav_selection == "Home":
    st.title("Welcome to Home Page")
    st.write("This is the homepage of the app.")
elif nav_selection == "Movies":
    st.title("Movies Page")
    st.write("You selected:", optionmovie)
    if st.button("movie recomanded", type="primary"):
        names, posters = recomanded(optionmovie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f'<p style="color:aqua;">{names[0]}</p>', unsafe_allow_html=True)
            st.image(posters[0])
        with col2:
            st.markdown(f'<p style="color:aqua;">{names[1]}</p>', unsafe_allow_html=True)
            st.image(posters[1])
        with col3:
            st.markdown(f'<p style="color:aqua;">{names[2]}</p>', unsafe_allow_html=True)
            st.image(posters[2])
        with col4:
            st.markdown(f'<p style="color:aqua;">{names[3]}</p>', unsafe_allow_html=True)
            st.image(posters[3])
        with col5:
            st.markdown(f'<p style="color:aqua;">{names[4]}</p>', unsafe_allow_html=True)

            st.image(posters[4])
    # Add your movie-related content here
elif nav_selection == "About":
    st.title("About Page")
    st.write("This is an app for movie recommendations.")

st.image("https://www.medianama.com/wp-content/uploads/2021/11/Android_Collage_1920x1080__UCAN_En.jpg")
footer_temp = """
<!doctype html>
<html lang="en">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

  <head>
  </head>
  <body>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Play&display=swap" rel="stylesheet"> 
</head>
<body>
<footer>
<div class="footer">
<div class="row">
<a href="#"><i class="fa fa-facebook"></i></a>
<a href="#"><i class="fa fa-instagram"></i></a>
<a href="#"><i class="fa fa-youtube"></i></a>
<a href="#"><i class="fa fa-twitter"></i></a>
</div>

<div class="row">
<ul>
<li><a href="#">Contact us</a></li>
<li><a href="#">Our Services</a></li>
<li><a href="#">Privacy Policy</a></li>
<li><a href="#">Terms & Conditions</a></li>
<li><a href="#">Career</a></li>
</ul>
</div>

<div class="row">
INFERNO Copyright © 2021 Inferno - All rights reserved || Designed By: Mahesh 
</div>
</div>
</footer>
  </body>
</html>
"""
st.markdown(footer_temp, unsafe_allow_html=True)