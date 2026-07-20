import streamlit as st
import pandas as pd
import pickle
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your preferences using KNN.")
with open("knn_model.pkl", "rb") as f:
    knn = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)
st.sidebar.header("Movie Preferences")

genre = st.sidebar.selectbox(
    "🎭 Genre",
    sorted(movies["Genre"].dropna().unique()),
    index=None,
    placeholder="Select Genre"
)

lead_star = st.sidebar.selectbox(
    "⭐ Lead Star",
    sorted(movies["Lead_Star"].dropna().unique()),
    index=None,
    placeholder="Select Lead Star"
)

director = st.sidebar.selectbox(
    "🎬 Director",
    sorted(movies["Director"].dropna().unique()),
    index=None,
    placeholder="Select Director"
)

music_director = st.sidebar.selectbox(
    "🎵 Music Director",
    sorted(movies["Music_Director"].dropna().unique()),
    index=None,
    placeholder="Select Music Director"
)

k = st.sidebar.slider(
    "Number of Recommendations",
    1,
    min(20, len(movies)),
    5
)
if st.sidebar.button("🎯 Recommend Movies"):

    query = pd.DataFrame({
        "Genre": [genre],
        "Lead_Star": [lead_star],
        "Director": [director],
        "Music_Director": [music_director]
    })

    query_encoded = encoder.transform(query)

    distances, indices = knn.kneighbors(
        query_encoded,
        n_neighbors=k
    )

    st.success(f"Top {k} Recommended Movies")

    for i, index in enumerate(indices[0]):

        movie = movies.iloc[index]

        similarity = (1 - distances[0][i]) * 100

        with st.container():

            st.markdown("---")

            st.subheader(f"🎥 {movie['Movie_Name']}")

            st.write(f"**Genre:** {movie['Genre']}")
            st.write(f"**Lead Star:** {movie['Lead_Star']}")
            st.write(f"**Director:** {movie['Director']}")
            st.write(f"**Music Director:** {movie['Music_Director']}")
            st.write(f"**Similarity:** {similarity:.2f}%")

else:
    st.info("👈 Select your preferences from the sidebar and click **Recommend Movies**.")