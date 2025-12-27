import streamlit as st
import pandas as pd
import numpy as np

# TITLE
st.title("✈️ Seni Perjalanan: Menemukan Kedamaian di Setiap Destinasi")

# HEADER & SUBHEADER
st.header("🏝️Perjalanan Eksklusif untuk Harmoni Jiwa")
st.subheader("Rasakan standar baru perjalanan eksklusif yang dirancang untuk kenyamanan dan ketenangan")

# TEXT / PARAGRAPH
st.text(
    "Kami percaya bahwa kemewahan sejati adalah ketenangan pikiran💞. "
    "Setiap destinasi dikurasi secara personal untuk menghadirkan "
    "privasi, kenyamanan, dan keheningan alam yang menenangkan, "
    "menciptakan pengalaman perjalanan yang membekas dan penuh makna💜."
)

# CODE (POTONGAN CODE)
st.subheader("Perhitungan Skor Ketenangan Perjalanan")
st.code(
    """
df["Skor Ketenangan Total"] = (
    df["Durasi Perjalanan (hari)"] * df["Indeks Ketenangan"]
)
    """,
    language="python"
)

# DATA DISPLAY (DATAFRAME / TABLE)
st.header("Data Destinasi Favorit")

data = {
    "Destinasi": ["Bali", "Kyoto", "Santorini", "Swiss Alps", "Maldives"],
    "Jenis Perjalanan": ["Relaksasi", "Budaya", "Romantis", "Alam", "Privasi"],
    "Tingkat Ketenangan": [9, 8, 8, 9, 10]
}

df = pd.DataFrame(data)
st.dataframe(df)

# CAPTION
st.caption(
    "Tabel ini menampilkan destinasi favorit yang dipilih berdasarkan tingkat ketenangan "
    "dan kenyamanan perjalanan."
)

# CHART
st.header("Visualisasi Tingkat Ketenangan Destinasi")
st.bar_chart(
    df.set_index("Destinasi")["Tingkat Ketenangan"]
)

# CAPTION
st.caption(
    "Visualisasi ini menggambarkan tingkat ketenangan tiap destinasi berdasarkan "
    "durasi perjalanan dan indeks kenyamanan."
)
