import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dashboard Penjualan Day 7")
st.write("Dashboard sederhana buat liat tren penjualan per produk")

# Load data - pake file csv yg sama kayak Day6
df = pd.read_csv('data_penjualan_day1.csv')

# Sidebar filter
produk_list = df['produk'].unique()
produk_pilih = st.sidebar.multiselect("Pilih Produk:", produk_list, default=produk_list)

# Filter data
df_filter = df[df['produk'].isin(produk_pilih)]

# Grafik
st.subheader("Total Penjualan per Produk")
fig, ax = plt.subplots()
df_filter.groupby('produk')['penjualan'].sum().plot(kind='bar', ax=ax, color='skyblue')
ax.set_ylabel("Total Penjualan")
st.pyplot(fig)

st.success("Dashboard jalan! Coba ganti filter di sidebar kiri 👈")
