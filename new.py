import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center;'>PollVue</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Public opinion lens!</h4>", unsafe_allow_html=True)
    
    # List of local image file paths
    image_paths = [
        "images/image1.jpg",
        "images/image2.jpg",
        "images/image3.jpg"
    ]
    
    # Initialize the session state for the current image index
    if 'current_image' not in st.session_state:
        st.session_state.current_image = 0

    # Display the current image
    current_image = st.session_state.current_image
    if 0 <= current_image < len(image_paths):
        st.image(image_paths[current_image], use_column_width=True)
    else:
        st.warning("No image to display.")

    # Buttons to navigate through images
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        if st.button("←"):
            st.session_state.current_image = (current_image - 1) % len(image_paths)
    
    with col3:
        if st.button("→"):
            st.session_state.current_image = (current_image + 1) % len(image_paths)

if __name__ == "__main__":
    main()

