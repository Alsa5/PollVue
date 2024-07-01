import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from datetime import datetime

if not firebase_admin._apps:
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

def fetch_posts_from_firestore(collection_name, limit=30):
    posts_ref = db.collection(collection_name).limit(limit)
    docs = posts_ref.stream()
    posts = []
    for doc in docs:
        post_data = doc.to_dict()
        posts.append([
            post_data.get('title', ''),
            post_data.get('score', 0),
            doc.id,
            post_data.get('subreddit', ''),
            post_data.get('url', ''),
            post_data.get('num_comments', 0),
            datetime.fromtimestamp(post_data.get('created', 0) / 1000),  # Convert timestamp to datetime
            post_data.get('body', '')
        ])
    return pd.DataFrame(posts, columns=["Title", "Score", "ID", "Subreddit", "URL", "Comments", "Created", "Body"])

def main():
    st.markdown("<h1 style='text-align: center;'>PollVue</h1>", unsafe_allow_html=True)
    st.image("https://www.imf.org/external/pubs/ft/fandd/2020/06/images/frieden-1600.jpg", caption="Indian Politics Dashboard", use_column_width=True)


    limit = st.sidebar.slider("Number of Posts", min_value=10, max_value=30, value=10)

    if st.sidebar.button("Fetch Posts from Firestore"):
        with st.spinner("Fetching posts..."):
            posts_df = fetch_posts_from_firestore("politics100", limit)
            st.success("Posts fetched successfully!")
            st.dataframe(posts_df)

            st.header("Summary Statistics")
            st.write(posts_df.describe())

            st.header("Posts")
            for i, row in posts_df.iterrows():
                st.subheader(row["Title"])
                st.write(f"Score: {row['Score']}, Comments: {row['Comments']}")
                st.write(row["Body"])
                st.write(f"[Link to post]({row['URL']})")
                st.write("---")

if __name__ == "__main__":
    main()