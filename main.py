import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Performance Ekspor Kopi Indonesia")
st.markdown("Kelvin Adhia Putra | Capstone Project")
st.markdown("Kopi merupakan salah satu komoditas unggulan Indonesia yang memiliki potensi besar dalam sektor ekspor. Indonesia dikenal sebagai salah satu produsen kopi terbesar di dunia dengan varietas yang beragam, seperti kopi Arabika dan Robusta yang memiliki cita rasa yang khas. Dengan pengelolaan yang baik dan peningkatan kualitas produk, ekspor kopi Indonesia dapat terus berkembang dan memberikan kontribusi positif terhadap perekonomian negara serta memperluas jangkauan pasar global.")
# Import CSV
data = pd.read_csv("Top 9.csv")

# Convert numeric values
tahun_cols = [col for col in data.columns if col.isdigit()]
data[tahun_cols] = data[tahun_cols].apply(
    lambda x: x.str.replace(',', '')).astype(float)

# Display line chart
data_melted = data.melt(id_vars='Negara Tujuan',
                        value_vars=tahun_cols, var_name='Tahun', value_name='Ton')
fig = px.line(data_melted, x='Tahun', y='Ton',
              color='Negara Tujuan', title='Ekspor Kopi Indonesia 2000 - 2022')
st.plotly_chart(fig)

st.markdown("Pada tahun 2022 sendiri terjadi kenaikan permintaan ekspor untuk negara-negara seperti Amerika Serikat, Mesir, Malaysia dengan volume kenaikan ekspor nasional sebesar 12,92% dari tahun sebelumnya. Untuk pasar Jepang akan mengalami kemunduran setelah ditemukannya bahan kimia Isoprocarb di bijih kopi Indonesia.")

# Remove commas and convert numeric values
data['Jumlah'] = data['Jumlah'].str.replace(',', '').astype(float)

# Sort the data by 'Jumlah' column in descending order
data_sorted = data.sort_values('Jumlah', ascending=False)

# Set the number of top destination countries to consider
top_countries = 9

# Select the top destination countries based on 'Jumlah'
top_countries_data = data_sorted.head(top_countries)

# Create an interactive bar chart using Plotly
fig = px.bar(top_countries_data, x='Jumlah', y='Negara Tujuan', orientation='h',
             color='Negara Tujuan', color_discrete_sequence=px.colors.qualitative.Safe)

# Customize the chart layout
fig.update_layout(
    title='Negara Tujuan Utama Ekspor Kopi Indonesia',
    xaxis_title='Jumlah Ekspor (Ton)',
    yaxis_title='Negara Tujuan',
    yaxis=dict(autorange="reversed"),
    barmode='stack',
    bargap=0.5,
)

# Display the chart in Streamlit
st.plotly_chart(fig)

st.markdown("Data menunjukkan bahwa Amerika Serikat dan negara Uni Eropa terutama Jerman dan Italia merupakan pasar utama dalam ekspor kopi di INdonesia. Disusul dengan Jepang dan negara - negara lain.")

# Membaca data dari CSV
data = pd.read_csv("Harga Kopi.csv")

# Membuat line chart menggunakan Plotly
fig = px.line(data, x="Year", y="Global Price (Us Dollar/lbs)",
              title="Harga Kopi Per Tahun")
fig.update_xaxes(title="Tahun")
fig.update_yaxes(title="Harga Global (Dolar AS/lbs)")

# Menampilkan chart menggunakan Streamlit
st.plotly_chart(fig)

st.markdown(
    "Kenaikan harga kopi global yang signifikan diperkirakan dari suplai langka akibat perubahan iklim untuk negara eksportir utama seperti Brazil dan Kolombia. Indonesia sendiri terancam mengalami penurunan produksi akibat harga pupuk, biaya pertanian yang semakin mahal, dan ancaman adanya El Nino.")
st.markdown("Melihat dari tren permintaan pada negara-negara Uni Eropa dan Amerika Serikat yang mengalami peningkatan bisa dikatakan ekspor kopi Indonesia masih akan terus mengalami peningkatan. Namun, pasar global yang tidak stabil dan kesejahteraan petani Indonesia yang masih mengalami kesusahan menjadi tantangan tersendiri bagi para eksportir kopi.")
