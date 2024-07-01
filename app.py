import streamlit as st  # Import Streamlit library for building web apps
from helpers import *  # Import helper functions from the helpers module

# Define the main function for the Streamlit web app
def main():
    # Set page configuration for the web app
    st.set_page_config(page_title="Bill Extractor")
    st.title("Bill Extractor AI Assistant...🤖")  # Display title on the web app

    # Upload Bills
    pdf_files = st.file_uploader(
        "Upload your bills in PDF format only", type=["pdf"], accept_multiple_files=True
    )  # Add a file uploader widget for uploading PDF bills

    extract_button = st.button("Extract bill data...")  # Add a button to trigger data extraction

    if extract_button:  # If the extract button is clicked
        with st.spinner("Extracting... it takes time..."):  # Display a spinner while extracting data
            data_frame = create_docs(pdf_files)  # Call the create_docs function to extract data
            st.write(data_frame.head())  # Display the first few rows of the extracted data

            # Clean and process the data (remove dollar symbols, convert to float, calculate average)
            data_frame["AMOUNT"] = data_frame["AMOUNT"].replace('[\$,]', '', regex=True).astype(float)
            st.write("Average bill amount: ", data_frame["AMOUNT"].mean())  # Display average bill amount

            # Convert the data frame to CSV format and prepare for download
            convert_to_csv = data_frame.to_csv(index=False).encode("utf-8")

            # Add a download button for downloading the data as a CSV file
            st.download_button(
                "Download data as CSV",
                convert_to_csv,
                "CSV_Bills.csv",
                "text/csv",
                key="download-csv",
            )
        st.success("Success!!")  # Display success message after data extraction and download

# Invoking the main function when the script is executed directly
if __name__ == "__main__":
    main()