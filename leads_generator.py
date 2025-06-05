import streamlit as st
import random
import string
import pandas as pd

def generate_fake_leads(keyword, count=10):
    leads = []
    for _ in range(count):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        number = '9' + ''.join(random.choices(string.digits, k=9))
        leads.append([name, number])
    return leads

st.title("🧠 Buyer Leads Generator")

st.markdown("Generate random buyer contact leads for property marketing.\n")

keyword = st.text_input("Enter keyword (e.g. 1BHK in Chembur)")
num_leads = st.slider("How many leads you want?", 5, 50, 10)

if st.button("🚀 Generate Leads"):
    if not keyword.strip():
        st.warning("❗ Please enter keyword!")
    else:
        leads = generate_fake_leads(keyword, num_leads)
        df = pd.DataFrame(leads, columns=["Name", "Contact Number"])
        st.success(f"✅ {len(leads)} leads generated for: **{keyword}**")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download leads as CSV",
            data=csv,
            file_name='leads.csv',
            mime='text/csv'
        )