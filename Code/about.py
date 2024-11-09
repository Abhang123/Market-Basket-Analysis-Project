import streamlit as st
from streamlit_lottie import st_lottie
import json
def app():
    st.write("### Global Market Analysis.")
    st.write("\n")
    st.map()
    st.write("\n")
    st.write("---")
    
    st.write("### Market Basket Analysis is a heuristic approach used in retail sector.")
    st.write("### Primary aim of MBA technique is to predict the frequently purchased items. This enables the retailers/shopkeepers to increase their product deployment at a substantial rate.")
    
    with open("Animation1.json") as source:
        animation = json.load(source)

    st_lottie(animation)
    st.write("\n")
    st.write("---")


    st.write("### For instance a customer goes to a grocery shop.")
    st.write("### When he/she buys a bread packet, then it is quite obvious that he/she will buy butter or milk.Thus to find the probability of the products that c=will be purchased along with the primary itmes is the aim of Market Basket Analysis technique.")
    st.write("")

    st.write("\n")
    st.write("---")
    


    










