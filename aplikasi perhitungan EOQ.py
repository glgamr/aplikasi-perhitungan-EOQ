import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi EOQ", layout="centered")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

st.markdown("""
Masukkan data berikut untuk menghitung jumlah pemesanan optimal (EOQ) dan melihat total biaya persediaan.
""")

# Input data
D = st.number_input("Permintaan tahunan (unit/tahun)", min_value=1.0, value=10000.0, step=100.0)
S = st.number_input("Biaya pemesanan per order (Rp)", min_value=1.0, value=100000.0, step=1000.0)
H = st.number_input("Biaya penyimpanan per unit per tahun (Rp)", min_value=1.0, value=5000.0, step=500.0)

# Tombol hitung
if st.button("🔍 Hitung EOQ dan Tampilkan Grafik"):
    # EOQ formula
    eoq = math.sqrt((2 * D * S) / H)
    jumlah_pemesanan = D / eoq
    total_biaya = (D / eoq) * S + (eoq / 2) * H

    # Tampilkan hasil
    st.success("✅ Hasil Perhitungan EOQ:")
    st.write(f"🔹 EOQ (Jumlah pemesanan optimal): **{eoq:.2f} unit**")
    st.write(f"🔹 Jumlah pemesanan per tahun: **{jumlah_pemesanan:.2f} kali**")
    st.write(f"🔹 Total biaya persediaan: **Rp {total_biaya:,.2f}**")

    # Grafik Total Biaya vs Jumlah Pemesanan (Q)
    Q_values = np.linspace(100, D, 200)  # rentang Q dari 100 hingga permintaan
    ordering_costs = (D / Q_values) * S
    holding_costs = (Q_values / 2) * H
    total_costs = ordering_costs + holding_costs

    # Plot
    fig, ax = plt.subplots()
    ax.plot(Q_values, total_costs, label="Total Biaya", color='blue')
    ax.axvline(eoq, color='red', linestyle='--', label=f"EOQ = {eoq:.2f}")
    ax.set_xlabel("Jumlah Pemesanan (Q)")
    ax.set_ylabel("Total Biaya Persediaan (Rp)")
    ax.set_title("Grafik Total Biaya vs Jumlah Pemesanan")
    ax.legend()
    ax.grid(True)

    # Tampilkan grafik di Streamlit
    st.pyplot(fig)
