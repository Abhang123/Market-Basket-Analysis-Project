import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from streamlit_lottie import st_lottie
import json
from apyori import apriori
import pickle
from mlxtend.frequent_patterns import fpgrowth, association_rules
def app():

    st.write("## Prediction of frequently purchased items.")
    st.write("\n")
    st.write("---")
    
    with open("animation5.json") as source:
        animation = json.load(source)

    st_lottie(animation, width = 800)

    st.write("\n")
    st.write("---")

    predict = st.button("PREDICT")
    
    if predict:
        st.write("\n")
        st.write("---")
        st.write("### Your dataset")
        st.write("\n")
        df = pd.read_csv("DATASET3.csv")
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

        

        # Display the DataFrame
        # print("Transaction Data:")
        
        # df1 = pd.get_dummies(df)
        # df2 = df1.iloc[:,1:]
    
        # # # Apply the FP-Growth algorithm
        # frequent_itemsets = fpgrowth(df2, min_support=0.002, use_colnames=True)

        # # # Convert itemsets to strings
        # frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: ', '.join(list(x)))

        # # # Display the frequent itemsets
        # # print("\nFrequent Itemsets:")
        # # print(frequent_itemsets)

        # # Generate the association rules
        # rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.07)
        # results = list(rules)
        # # Convert antecedents and consequents to strings
        # rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
        # rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

        # # Display the association rules
        # st.write("\nAssociation Rules:")
        # st.write(rules)       