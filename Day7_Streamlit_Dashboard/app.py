import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")
st.title("📊 Day 7: Dashboard Penjualan Interaktif")

uploaded_file = st.file_uploader("Upload CSV Penjualan", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data berhasil diupload!")
    
    # KPI
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Penjualan", f"Rp {df['harga'].sum():,.0f}")
    col2.metric("Total Qty", f"{df['jumlah'].sum():,}")
    col3.metric("Rata2 Harga", f"Rp {df['harga'].mean():,.0f}")
    
    # Grafik
    st.bar_chart(df.groupby('produk')['jumlah'].sum())
else:
    st.info("Silakan upload file CSV dulu bro")
