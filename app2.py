import streamlit as st  # Import Streamlit library for building web apps
from helpers_ko import *  # Import helper functions from the helpers module

# Define the main function for the Streamlit web app
def main():
    # Set page configuration for the web app
    st.set_page_config(page_title="영수증 추출기")
    st.title("국방전산정보원 영수증 추출 AI 🤖")  # Display title on the web app

    # Upload Bills
    pdf_files = st.file_uploader(
        "PDF 파일만 업로드하세요", type=["pdf"], accept_multiple_files=True
    )  # Add a file uploader widget for uploading PDF bills

    extract_button = st.button("영수증 데이터 추출...")  # Add a button to trigger data extraction

    if extract_button:  # If the extract button is clicked
        with st.spinner("추출하는 중... 시간이 조금 걸립니다..."):  # Display a spinner while extracting data
            data_frame = create_docs(pdf_files)  # Call the create_docs function to extract data
            st.write(data_frame.head())  # Display the first few rows of the extracted data

            # Clean and process the data (remove dollar symbols, convert to float, calculate average)
            data_frame["금액"] = data_frame["금액"].replace('[\$,]', '', regex=True).astype(float)
            st.write("평균 금액: ", data_frame["금액"].mean())  # Display average bill amount

            # Convert the data frame to CSV format and prepare for download
            convert_to_csv = data_frame.to_csv(index=False, encoding='utf-8-sig').encode("utf-8-sig")

            # Add a download button for downloading the data as a CSV file
            st.download_button(
                "CSV 파일로 데이터 다운로드",
                convert_to_csv,
                "CSV_Bills.csv",
                "text/csv",
                key="download-csv",
            )
        st.success("성공!!")  # Display success message after data extraction and download

# Invoking the main function when the script is executed directly
if __name__ == "__main__":
    main()