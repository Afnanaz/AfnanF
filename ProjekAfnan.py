import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import streamlit as st 

customers_df = pd.read_csv("https://raw.githubusercontent.com/Afnanaz/AfnanF/main/customers_dataset.csv")
payment_df = pd.read_csv("https://raw.githubusercontent.com/Afnanaz/AfnanF/main/order_payments_dataset.csv")
productcat_df = pd.read_csv("https://raw.githubusercontent.com/Afnanaz/AfnanF/main/productcat_df_cleaned.csv")

# Header
st.header("Visualisasi Data E-commerce Brazil")

def create_total_orders(df):
    total = pd.value_counts(values=df['customer_id']).sum()
   
    return total

def create_total_payments(df):
    total = df['payment_value'].sum()

    return "${}".format(total)

def create_total_category(df):
    total = df['product_category_name'].nunique()

    return total

total_payments = create_total_payments(payment_df)
total_orders = create_total_orders(customers_df)
total_category = create_total_category(productcat_df)


col1_1, col1_2, col1_3 = st.columns(spec=3)

with col1_1:
    st.metric(label="Total Payments", value=total_payments)

with col1_2:
    st.metric(label="Total Orders", value=total_orders)

with col1_3:
    st.metric(label="Total Category", value=total_category)

top5_customers = customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).head(5)

# Mengatur ukuran dan membuat satu sumbu (axes)
fig, ax = plt.subplots(figsize=(12, 6))  

# Membuat bar plot
top5_customers.plot(kind='bar', color='skyblue', ax=ax)  

# Menambahkan judul dan label sumbu
st.subheader('Top 5 Kota dengan Pembeli Terbanyak')
ax.set_xlabel('State')
ax.set_ylabel('Number of Customers')
ax.tick_params(axis='x', rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


st.pyplot(fig)

# Ambil data pembayaran untuk setiap metode pembayaran
payment_each_method = payment_df.groupby(by="payment_type")["payment_value"].sum().reset_index()

# Cari indeks dari jenis pembayaran terbesar
max_index = payment_each_method["payment_value"].idxmax()

# Hitung persentase maksimum
max_percentage = payment_each_method["payment_value"].iloc[max_index] / payment_each_method["payment_value"].sum() * 100

# Buat pie chart
st.subheader('Metode Pembayaran yang Paling Banyak Digunakan')
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(payment_each_method["payment_value"], labels=['' if i != max_index else f'{payment_each_method["payment_type"].iloc[i]}: {max_percentage:.1f}%' for i in range(len(payment_each_method))], autopct=lambda pct: f'{pct:.1f}%' if pct > max_percentage else '', startangle=140)
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
plt.tight_layout()

# Menampilkan gambar menggunakan streamlit
st.pyplot(fig)

import matplotlib.pyplot as plt
import streamlit as st

# Visualizing the number of unique products
fig, ax = plt.subplots(figsize=(10, 6))  # Membuat subplot dengan ukuran yang diinginkan
product_count = productcat_df.groupby(by="product_category_name")["product_id"].nunique().head(5)
product_count.plot(kind='bar', color='skyblue', ax=ax)  # Menggunakan objek sumbu ax

st.subheader('Top 5 Kategori Barang dengan Tinggi Pembeli')
ax.set_xlabel('Product Category')
ax.set_ylabel('Number of Unique Products')
ax.tick_params(axis='x', rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Menampilkan gambar menggunakan Streamlit
st.pyplot(fig)





