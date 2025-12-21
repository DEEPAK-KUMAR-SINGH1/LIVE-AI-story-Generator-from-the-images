import streamlit as st
from story_generator import generate_story_from_images,narrate_story
from PIL import Image

st.title("AI story Generator from the images")
st.markdown("Upload 1 to 10 image , Choose any Style and let AI write and Narrate an story for you ")

with st.sidebar:
    st.header("Controls")

    # Sidebar option to upload images
    uploaded_files = st.file_uploader(
        "Upload your images ....",
        type=["png","jpg","jpeg"],
        accept_multiple_files=True
    )

    # Selecting an story style
    story_style = st.selectbox(
        "Choose a story style",
        ("Comedy","Thriller","Fairy tale","Sci-Fci","Mystery","Adventure","Morale")
    )

    # Button to Generate story
    generate_button = st.button(
        "Generate story and Narration ",
        type="primary"
    )

# Main logic
if generate_button:
    if not uploaded_files:
        st.warning("Please upload Atleast 1 image ")
    elif len(uploaded_files)>10:
        st.warning("Please uploade Maximum of 10 image")
    else:
        with st.spinner("The AI is writting and Narrating your story .... This will take few Moments."):
            try:
                pil_images = [Image.open(uploaded_file) for uploaded_file in uploaded_files]
                st.subheader("Your visual inspiration:")
                image_columns = st.columns(len(pil_images))

                for i ,image in enumerate(pil_images):
                    with image_columns [i]:
                        st.image(image,use_container_width=True)

                generate_story = generate_story_from_images(pil_images,story_style)
                if "error" in generate_story or "failed" in generate_story or "API KEY" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"YOUR {story_style} story :")
                    st.success(generate_story)

                st.subheader("Listen to your Story:")
                audio_file= narrate_story(generate_story)
                if audio_file:
                    st.audio(audio_file,format="audio/mp3")

            except Exception as e:
                st.error(f"An Application Error Occorred {e}")