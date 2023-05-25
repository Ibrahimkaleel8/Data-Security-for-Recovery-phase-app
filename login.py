import streamlit as st
import mysql.connector
from mysql.connector import Error
import home

#Establish connection to Mysql Server
def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password='Razik@123',
        database='user_info'
)
    return mydb

def main():
    st.title("Recovery Phase Encryption")
    menu = ("Login","SignUp","Home")
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Login":
        login()

    if choice == "SignUp":
        signup()

    if choice == "Home":
        home.home()


def login():
    st.subheader("Login Section")
    mydb = create_connection()
    mycursor = mydb.cursor()
    User_Name = st.text_input("User Name")
    password = st.text_input("Password",type='password')
    if st.button("Login"):
        sql = "SELECT * FROM users WHERE User_Name = %s AND password = %s"
        val = (User_Name,password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            st.success("You can directed to homepage")
        else:
            st.warning('Incorrect username or password.')
    mydb.close()


def signup():
    st.subheader("Create New Account")
    mydb = create_connection()
    mycursor = mydb.cursor()
    User_Name = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    if st.button("SignUp"):
        if password == confirm_password:
            try:
                sql="insert into users(User_Name,password) values(%s,%s)"
                val=(User_Name,password)
                mycursor.execute(sql,val)
                mydb.commit()
                st.info("You have successfully created an account")
                st.write("Go to Login Page")
            except Error as e:
                st.error("SignUp failed, Username already taken")
        else:
            st.warning("Password do not match")
    mydb.close()

if __name__ == '__main__':
    main()