from langchain.llms import OpenAI  # OpenAI API 래퍼 가져오기
from pypdf import PdfReader  # PyPDF 라이브러리의 PdfReader 가져오기
import pandas as pd  # 데이터 조작을 위해 pandas 가져오기
import re  # 정규 표현식을 위해 re 가져오기
from langchain.prompts import PromptTemplate  # 생성 프롬프트를 위해 langchain에서 PromptTemplate 가져오기
from langchain.chat_models import ChatOpenAI  # 대화 기반 상호작용을 위해 langchain에서 ChatOpenAI 가져오기
from langchain.agents.agent_types import AgentType  # 에이전트 유형을 위해 langchain에서 AgentType 가져오기

import openai  # OpenAI Python 라이브러리 가져오기
import os  # 시스템 관련 함수를 위해 os 가져오기
from dotenv import find_dotenv, load_dotenv  # 환경 변수를 불러오기 위해 dotenv에서 find_dotenv, load_dotenv 가져오기

load_dotenv(find_dotenv())  # .env 파일에서 환경 변수 불러오기
openai.api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 OpenAI API 키 설정

# DPDF 파일에서 텍스트 추출 기능을 정의
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# OpenAI API를 사용하여 텍스트에서 데이터를 추출하는 기능을 정의
def extracted_data(pages_data):
    # Define a template for the prompt to be sent to OpenAI API
    template = """주어진 페이지에서 다음 값들을 추출하세요: 계산서 번호, 설명, 발행일,
             단가, 금액, 청구 대상, 발행처 및 지불 조건: {pages}
             
             예상 출력: 모든 달러 기호 제거 {{'계산서 번호': '1001329', '설명': '단가', '금액': '2', '발행일': '2023/05/04', '금액': '1100.00', '청구 대상': '제임스', '발행처': '엑셀 컴퍼니', '지불 조건': '지금 결제하세요'}}
             """
    # Create a PromptTemplate object with the template
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)
    # Create an OpenAI object for language model interaction
    llm = OpenAI(temperature=0.7)
    # Generate a full response by formatting the prompt with pages_data and passing it to the OpenAI API
    full_response = llm(prompt_template.format(pages=pages_data))

    return full_response

# Define a function to create documents from uploaded PDFs
def create_docs(user_pdf_list):
    # Create a pandas DataFrame to store extracted data
    df = pd.DataFrame(
        {
            "계산서 번호": pd.Series(dtype="int"),
            "설명": pd.Series(dtype="str"),
            "발행일": pd.Series(dtype="str"),
            "단가": pd.Series(dtype="str"),
            "금액": pd.Series(dtype="int"),
            "청구 대상": pd.Series(dtype="str"),
            "발행처": pd.Series(dtype="str"),
            "지불 조건": pd.Series(dtype="str"),

        }
    )

    # 업로드된 각 PDF 파일 반복 처리
    for filename in user_pdf_list:
        raw_data = get_pdf_text(filename)  # PDF 파일에서 텍스트 추출
        llm_extracted_data = extracted_data(raw_data)  # OpenAI API를 사용해 데이터 추출

        # OpenAI API 응답에서 데이터를 추출하기 위해 정규 표현식 사용
        pattern = r"{(.+)}"  # 줄바꿈을 제외한 하나 이상의 모든 문자를 캡처
        match = re.search(pattern, llm_extracted_data, re.DOTALL)

        if match:
            extracted_text = match.group(1)
            # 추출된 텍스트를 사전으로 변환
            data_dict = eval("{" + extracted_text + "}")  #문자열을 사전으로 변환

            # 금액 데이터의 포맷을 정리
            if '금액' in data_dict:
                data_dict['금액'] = format(float(re.sub('[^\d.]', '', data_dict['금액'])), ",.0f")  # 쉼표 추가

            if '단가' in data_dict:
                data_dict['단가'] = format(float(re.sub('[^\d.]', '', data_dict['단가'])), ",.0f")  # 쉼표 추가
            else:
                data_dict['단가'] = "정보 없음"  # 단가 정보가 없는 경우 처리

            # Create a temporary DataFrame from extracted data and avoid duplication
            temp_df = pd.DataFrame([data_dict])
            # Concatenate to the main DataFrame
            df = pd.concat([df, temp_df], ignore_index=True)
        else:
            print("일치하는 데이터가 없습니다. 파일을 확인하세요.")

    # 중복 제거
    df = df.drop_duplicates()    

    #df.head()  # DataFrame의 처음 몇 행 표시
    return df  # 추출된 데이터를 포함하는 DataFrame 반환