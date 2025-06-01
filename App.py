import streamlit as st
import pandas as pd
import pickle
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Restaurant Dashboard App", layout="centered")
st.sidebar.header("Dashboard")

st.title("Selamat datang di aplikasi streamlit sederhana")
st.write("Aplikasi ini dibuat untuk demonstrasi projek akhir Data Mining.")

#Load Dataset
df = pd.read_csv("model/resto.csv")

#Tampilkan dataframe
st.subheader("Dataset Resto")
st.dataframe(df)

st.write(df.columns.tolist())
#df[target] = data target
#df['label'] = df['variety'].
