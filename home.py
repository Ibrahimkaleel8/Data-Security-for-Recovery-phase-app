import streamlit as st
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from cryptography.hazmat.primitives.ciphers.algorithms import AES
import algo1
import algo3
import text_extract
import mysql.connector



def home():
    text_extract.extract()
    st.subheader("Select your operations")
    key = st.radio("", ('Store', 'Access'))

    if key == "Store":
        encrypt()

    if key == "Access":
        decrypt()

def save_to_mysql(result, data_type):
    #save result to text file
    filename = "encrypted_result.txt"
    with open(filename, "wb" if data_type == "bytes" else "w") as file:
        file.write(result)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password='Razik@123',
        database='user_info'
    )
    cursor = conn.cursor()

    # Read the content of the text file
    with open(filename, "rb" if data_type == "bytes" else "r") as file:
        content = file.read()
    query = "INSERT INTO users (result) VALUES (%s)"
    cursor.execute(query, (content,))
    conn.commit()
    conn.close()

def encrypt():
    st.subheader("Select your Keys")
    keys = st.selectbox("", ('iphone','Nokia'))

    if keys == "iphone":
        with st.form(key='my_form'):
            input_s = st.text_input("Enter Recovery_Phase")
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:

                result1= algo1.algo1_encrypt(input_s)

                # Create a file and write user input to it
                save_to_mysql(result1, data_type="str")

                # Show success message to the user
                st.write("Encrypted texts stored in Blockchain!")

        #string_encrypted = algo1.algo1_encrypt(input_s)
        #string_decrypted = algo1.algo1_decrypt(result)
        #print("encrypted strings: ", result)
        #print("decrypted strings: ", string_decrypted)


    if keys == "Nokia":
        with st.form(key='my_form'):
            plaintext = st.text_input("Enter Recovery_Phase")
            key = os.urandom(32)
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                # Do something when the button is clicked
                result2 = algo3.algo3_encrypt(cipher, plaintext)
                # decrypted_plaintext = algo3.algo3_decrypt(cipher, ciphertext_bytes)
                # Create a file and write user input to it
                save_to_mysql(result2, data_type="bytes")

                # Show success message to the user
                st.write("Encrypted texts stored in Blockchain!")

def decrypt():
    st.subheader("Select your Keys")
    keys = st.selectbox("", ('iphone', 'Nokia'))

    if keys == "iphone":
        with st.form(key='decrypt_form'):
            input_s = st.text_input("Enter Encrypted_Text")
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                decrypted_result = algo1.algo1_decrypt(input_s)
                st.write("Decrypted Text: ", decrypted_result)

    if keys == "Nokia":
        with st.form(key='decrypt_form'):
            input_s = st.text_input("Enter Encrypted_Text")
            key = os.urandom(32)
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                padder = padding.PKCS7(AES.block_size).padder()
                padded_input = padder.update(input_s.encode('utf-8')) + padder.finalize()

                decrypted_result = algo3.algo3_decrypt(cipher, padded_input)
                st.write("Decrypted Text: ", decrypted_result)