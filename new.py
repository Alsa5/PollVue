import streamlit as st
import login 
def main():
    st.markdown("<h1 style='text-align: center;'>PollVue</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Public opinion lens!</h4>", unsafe_allow_html=True)
    # List of image URLs related to politics
    image_urls = [
        "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hbEgvBf99ZyrgZ28iD0BnQ.jpeg",
        "https://media.licdn.com/dms/image/D5612AQHEeG5WXk4GQA/article-cover_image-shrink_720_1280/0/1684161928638?e=1725494400&v=beta&t=XcA1QZ8xJ7gYuxzK_kWvg7p0XZZrylwwfjew5kDRsGg",
        "https://sc0.blr1.cdn.digitaloceanspaces.com/article/133739-jwdykatblz-1577670825.jpeg",
        
    ]
    
    # Initialize the session state for the current image index
    if 'current_image' not in st.session_state:
        st.session_state.current_image = 0

    # Display the current image
    current_image = st.session_state.current_image
    st.image(image_urls[current_image], use_column_width=True)

    # Buttons to navigate through images
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        if st.button("←"):
            st.session_state.current_image = (current_image - 1) % len(image_urls)
    
    with col3:
        if st.button("→"):
            st.session_state.current_image = (current_image + 1) % len(image_urls)

    


if __name__ == "__main__":
    main()


