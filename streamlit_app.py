import streamlit as st
import pandas as pd
import json

st.caption("This is a demo")

option = st.selectbox(
    "Choose a Cloud Service Provider",
    ("GCP", "Azure", "AWS"),placeholder="Select the Cloud Platform You Want to Compare")

st.write("You selected:", option)

if option=="Azure":

    # Load data
    with open('azure.json', 'r') as file:
        data = json.load(file)

    # Extract relevant fields and create a DataFrame
    items = data['Items']
    df = pd.DataFrame(items)

    # Filter relevant columns and rename them
    df_filtered = df[['serviceFamily', 'meterId', 'retailPrice', 'armRegionName']].copy()
    df_filtered.columns = ['Family', 'ID', 'Price', 'Region']

    # Function to get the cheapest VM per region
    def get_cheapest_vm_per_region(df):
        return df.loc[df.groupby('Region')['Price'].idxmin()]

    # Add a multiselect filter for regions
    selected_regions = st.multiselect("Select Regions", options=df_filtered['Region'].unique())

    # Filter the DataFrame based on selected regions
    filtered_df = df_filtered[df_filtered['Region'].isin(selected_regions)]

    # Get the cheapest VM per selected region
    cheapest_vms = get_cheapest_vm_per_region(filtered_df)

    # Display the DataFrame
    st.title("Azure VM Pricing")
    st.dataframe(cheapest_vms.sort_values(by=['Region', 'Price']),st.column_config)

    # Display all VMs with the cheapest ones on top for each region
    st.title("All Azure VM Pricing (Cheapest on top for each region)")
    st.dataframe(filtered_df.sort_values(by=['Region', 'Price']))

    # Run the Streamlit app
    if __name__ == '__main__':
        st.caption("Made with Love; Team Brio   ")
