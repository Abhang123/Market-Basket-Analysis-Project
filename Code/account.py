import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
from streamlit_lottie import st_lottie
import json

cred = credentials.Certificate("mba-app-25be9-2fb5c2a5685f.json")
#firebase_admin.initialize_app(cred)
def app(): 
    
    st.title('Market Basket:violet[ Analysis Web App]')
    with open("anima1.json") as source:
        animation = json.load(source)

    st_lottie(animation, width = 800)

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False

    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('**Login/Signup**',['Login','Sign up'])
        email = st.text_input('**Email Address**')
        password = st.text_input('**Password**',type='password')
        
        if choice == 'Sign up':
            username = st.text_input("**Enter your unique username**")
            
            if st.button('**Create my account**'):
                user = auth.create_user(email = email, password = password,uid=username)
                
                st.success('**Account created successfully!**')
                st.markdown('**Please Login using your email and password**')
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                st.text('Name '+st.session_state.username)
                st.text('Email id: '+st.session_state.useremail)
                st.button('Sign out', on_click=t) 
            
                                 
    def run():
        st.write('Posts')





        














