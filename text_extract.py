import streamlit as st
import keras_ocr
import re
import pandas as pd
import matplotlib.pyplot as plt

def extract_alpha_characters(text):
    # Remove numericals and special characters using regular expressions
    alpha_characters = re.sub('[^a-zA-Z]', '', text)

    return alpha_characters

def extract():
    st.subheader("Character Extraction")

    # Ask the user to upload the image file
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png", "webp"])
    submit_button = st.button("Submit")

    if submit_button and uploaded_file is not None:
        try:
            pipeline = keras_ocr.pipeline.Pipeline()
            image = plt.imread(uploaded_file)
            prediction_groups = pipeline.recognize([image])
            predicted_image = prediction_groups[0]
            alpha_texts = []

            for text, box in predicted_image:
                alpha_text = extract_alpha_characters(text)
                alpha_texts.append(alpha_text)

            result = ' '.join(alpha_texts)

            st.success("Characters Extracted:")
            st.write(result)

        except Exception as e:
            st.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    extract()
