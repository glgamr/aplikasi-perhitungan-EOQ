import streamlit as st
import math

# Judul aplikasi
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

# Deskripsi
st.markdown("""
Simulasi sistem persediaan untuk menghitung **jumlah pemesanan optimal (EOQ)** berdasarkan input berikut:
- Permintaan tahunan
- Biaya pemesanan
- Biaya penyimpanan
""")

# Input pengguna
D = st.number_input("Permintaan tahunan (unit/tahun)", min_value=1.0, step=1.0)
S = st.number_input("Biaya pemesanan per order (Rp)", min_value=0.0, step=100.0)
H = st.number_input("Biaya penyimpanan per unit per tahun (Rp)", min_value=0.0, step=100.00)

# Tombol Hitung
if st.button("Hitung EOQ"):
    if D > 0 and S > 0 and H > 0:
        eoq = math.sqrt((2 * D * S) / H)
        jumlah_pemesanan = D / eoq
        total_biaya = (D / eoq) * S + (eoq / 2) * H

        # Hasil Output
        st.success("✅ Hasil Perhitungan:")
        st.write(f"🔹 **EOQ (Jumlah pemesanan optimal)**: `{eoq:.2f}` unit")
        st.write(f"🔹 **Jumlah pemesanan per tahun**: `{jumlah_pemesanan:.2f}` kali")
        st.write(f"🔹 **Total biaya persediaan**: `Rp {total_biaya:,.2f}`")
    else:
        st.warning("❗ Semua input harus lebih dari 0.")
