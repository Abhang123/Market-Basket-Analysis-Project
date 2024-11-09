import pandas as pd
import streamlit as st
import databaseObject 
import numpy as np
import matplotlib.pyplot as plt 
from streamlit_lottie import st_lottie
import json
from apyori import apriori

st.write("\n")
st.write("---")

def fetch_firestore_data(collection_name):
    # Retrieve data from Firestore collection
    docs = databaseObject.dbObj().collection(collection_name).stream()
    # Initialize an empty list to store document data
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    return data

def display_data_as_table(data):
    # Convert data to pandas DataFrame
    df = pd.DataFrame(data)
    # Display DataFrame as table
    print(df)


def app():
    # Replace 'your_collection_name' with the name of your Firestore collection
    # Create a form
    with st.form(key='my_form'):
        # Add a text input
        collection_name = st.text_input(label='Enter Your Username ')
        submit_button = st.form_submit_button(label='Submit')
    # Check if the form has been submitted
    if submit_button:
        # Get the values of the form inputs
        # collection_name = name.value
        # st.write(f'Name: {name}')
    # Fetch data from Firestore
        data = fetch_firestore_data(collection_name)
        # df = pd.json_normalize(df)
        print(data)
    # Display data as table
        st.table(data)

    predict = st.button("PREDICT")
    
    if predict:
        st.write("\n")
        st.write("---")
        st.write("### Your dataset")
        st.write("\n")
        df = fetch_firestore_data(collection_name)
        df = pd.json_normalize(df)
        st.dataframe(df, width = 800)

        st.write("\n")
        st.write("---")

        figure = plt.figure()
        Item_distr = df.groupby(by = 'itemDescription').size().reset_index(name = 'Frequency').sort_values(by = 'Frequency', ascending = False).head(10)
        bars = Item_distr['itemDescription']
        height = Item_distr['Frequency']
        index = np.arange(len(bars))
        plt.xlabel("Item names")
        plt.ylabel("Frequency")
        plt.bar(index, height, color = (0.1,0.3,0.5,0.7))
        plt.xticks(index,bars)
        plt.gcf().autofmt_xdate()
        plt.plot(index, height)
        st.write("### Graph showing frequently purchased items.")
        st.write("\n")
        st.write(figure, width = 700)
        st.write("\n")
        st.write("---")

        customer_level = df[['Member_number', 'itemDescription']].sort_values(by = 'Member_number', ascending = False)
        customer_level['itemDescription'] = customer_level['itemDescription'].str.strip()

        transactions  = [a[1]['itemDescription'].tolist() for a in list(customer_level.groupby(["Member_number"]))]

        # Implementation of Apriori algorithm

        rules = apriori(transactions = transactions, min_support = 0.002, min_confidence = 0.05, min_lift = 3, min_length = 2)
        results = list(rules)


        def inspect(results):
                LHS = [tuple(result[2][0][0])[0] for result in results]
                RHS = [tuple(result[2][0][1])[0] for result in results]
                supports = [result[1] for result in results]
                confidences = [result[2][0][2] for result in results]
                lifts = [result[2][0][3] for result in results]
                return list(zip(LHS, RHS, supports, confidences, lifts))

        resultsindataframe = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidences', 'Lift'])
        st.write("\n")
        st.write("Table showing frequent itemsets and their relationship")
        st.write("\n")
        st.write(resultsindataframe.nlargest(n = 10, columns = "Lift"), width = 500, height = 500)
        st.write("\n")
        st.write("---")
        



        
    
        


        











