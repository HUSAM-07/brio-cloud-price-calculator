import streamlit as st
import pandas as pd

st.title("Brio Technologies Internal Cloud Price Calculator")
# Sample data similar to the provided image
data = {
    'VM Name': ['Basic_A0', 'Basic_A1', 'Basic_A2', 'Basic_A3', 'Basic_A4', 'Standard_A0', 'Standard_A1', 'Standard_A1_v2', 'Standard_A2', 'Standard_A2_v2'],
    'vCPUs': [1, 1, 2, 4, 8, 1, 1, 1, 2, 2],
    'Memory (GiB)': [0.75, 1.75, 3.5, 7, 14, 0.75, 1.75, 2, 3.5, 3.5],
    'Linux Price': [0.0180, 0.0230, 0.0790, 0.1760, 0.3520, 0.0200, 0.0600, 0.0430, 0.1200, 0.1200],
    'Windows Price': [0.0180, 0.0320, 0.1330, 0.2960, 0.5920, 0.0200, 0.0900, 0.0650, 0.1800, 0.1800],
    'Alternative VMs': ['find better']*10,
    'Savings Options': ['compare']*10,
    'Best Price Region / Diff': ['Korea South / -11.1%', 'US Gov Virginia / -5.2%', 'US Gov Virginia / -21.8%', 'US Gov AZ / -9.1%', 'US Gov TX / -9.1%', 'Korea South / -10%', 'West Central US / -15%', 'West US 2 / -16.3%', 'West Central US / -15.8%', 'West Central US / -15.8%']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Azure VM Comparison")
st.set_page_config(page_title="Brio's Internal Tool", page_icon="☁️")
# Input fields
currency = st.selectbox('Currency', ['US Dollar ($)', 'Euro (€)', 'British Pound (£)'])
region = st.selectbox('Region', ['East US (Virginia) / eastus', 'West US (California) / westus', 'Central US (Iowa) / centralus'])
pricing_model = st.selectbox('Pricing Model', ['Pay as-you-go', 'Reserved'])
vcpus = st.slider('Number of vCPUs', 1, 416, (1, 4))
memory = st.slider('Memory (GiB)', 0.5, 11400.0, (0.5, 8.0))

# Filter the data based on input
filtered_df = df[(df['vCPUs'] >= vcpus[0]) & (df['vCPUs'] <= vcpus[1]) & (df['Memory (GiB)'] >= memory[0]) & (df['Memory (GiB)'] <= memory[1])]

# Display the filtered data
st.dataframe(filtered_df)
