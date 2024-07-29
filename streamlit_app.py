import streamlit as st
import requests
import pandas as pd

# Function to fetch Azure VM pricing data
def fetch_azure_vm_prices():
    url = "https://catalogapi.azure.com/skus?api-version=2023-05-01-preview&serviceFamily=Compute&service=Virtual Machines&language=en&locations=US East 2"
    response = requests.get(url)
    data = response.json()
    
    items = data['Items']
    return items

# Function to process Azure VM pricing data
def process_azure_data(items):
    azure_data = []

    for item in items:
        if 'serviceFamily' in item and item['serviceFamily'] == 'Compute':
            azure_data.append([
                item['productName'],
                item['armSkuName'],
                item['armRegionName'],
                item['retailPrice']
            ])

    df = pd.DataFrame(azure_data, columns=['Family', 'Core', 'Region', 'Price'])
    return df

# Streamlit app
st.title("Cloud VM Price Comparison")
st.header("Azure VM Pricing")

# Fetch and process Azure VM pricing data
azure_items = fetch_azure_vm_prices()
azure_df = process_azure_data(azure_items)

# Display Azure VM pricing data
st.dataframe(azure_df)
