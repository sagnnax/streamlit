import streamlit as st
import pandas as pd

st.title("Streamlit - Search ranges")
DATA_URL =  "https://firebasestorage.googleapis.com/v0/b/range-46ab6.appspot.com/o/dataset.csv?alt=media&token=61814926-8ebf-49a7-955e-019b0f367d91"

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL) #read csv
    filtered_data_byrange = data[ (data["index"] >= startid) & (data["index"] <= endid) ]

    return filtered_data_byrange #return the data frame

startid = st.text_input("Start index :" )
endid = st.text_input("End index :" )
btnRange = st.button("Search by range")


if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid)) #call the function
    count_row = filterbyrange.shape[0] #
    st.write(f"Total names : {count_row}")

    st.dataframe(filterbyrange)
