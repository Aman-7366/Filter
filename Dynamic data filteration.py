import pandas as pd
import streamlit as st

# Function to load and filter data
def load_data(file):
    data = pd.read_excel(file)  # Assuming the data is in Excel format
    return data

# Main function
def main():
    st.title("Dynamic Data Filter")
    
    # Upload file
    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    
    if uploaded_file is not None:
        # Load data
        df = load_data(uploaded_file)
        
        # Display raw data
        st.subheader("Raw Data")
        st.dataframe(df)

        # Filters
        st.sidebar.header("Filters")

        # Unique companies
        companies = df['NAME'].unique()
        selected_company = st.sidebar.selectbox("Select Company", companies)

        # Unique locations
        locations = df['LOCATION'].unique()
        selected_location = st.sidebar.selectbox("Select Location", locations)
        
        # Filter data based on selections
        filtered_data = df[(df['NAME'] == selected_company) & (df['LOCATION'] == selected_location)]
        
        # Display filtered data
        st.subheader("Filtered Data")
        st.dataframe(filtered_data)

if __name__ == "__main__":
    main()
