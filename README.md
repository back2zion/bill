<img width="1920" alt="20240701_capture" src="https://github.com/back2zion/bill/assets/17250308/c3325197-12c4-44e5-9730-72513fa2d889">


```markdown
# LLM 기반 영수증 데이터 추출 시스템

이 프로젝트는 PDF 형식의 영수증에서 데이터를 추출하여 CSV 파일로 변환하는 시스템입니다.
이 시스템은 LLM(대규모 언어 모델)을 활용하여 영수증의 정보를 자동으로 추출하고, 데이터를 정리하여 재정 관리에 활용할 수 있도록 합니다.

## 기능

- PDF 파일에서 영수증 데이터를 자동으로 추출
- 추출된 데이터를 CSV 파일로 변환
- 실시간 데이터 처리 및 분석
- 정확하고 일관된 데이터 관리

## 설치 및 실행

### 사전 요구사항

- Python 3.7 이상
- pip 패키지 관리자

### 설치

1. 저장소를 클론합니다.

```sh
git clone https://github.com/yourusername/receipt-extraction.git
cd receipt-extraction
```

2. 필요한 패키지를 설치합니다.

```sh
pip install -r requirements.txt
```

### 실행

1. `.env` 파일을 생성하고, OpenAI API 키를 설정합니다.

```plaintext
OPENAI_API_KEY=your_openai_api_key
```

2. Streamlit 웹 애플리케이션을 실행합니다.

```sh
streamlit run app2.py
```

## 사용 방법

1. 웹 애플리케이션을 실행한 후, PDF 영수증 파일을 업로드합니다.
2. "영수증 데이터 추출..." 버튼을 클릭하여 데이터를 추출합니다.
3. 추출된 데이터를 화면에서 확인하고, CSV 파일로 다운로드할 수 있습니다.

## 파일 설명

- `app2.py`: Streamlit 웹 애플리케이션의 메인 파일입니다.
- `helpers_ko.py`: PDF에서 텍스트를 추출하고 데이터를 처리하는 함수들이 포함된 헬퍼 파일입니다.
- `requirements.txt`: 필요한 Python 패키지 목록입니다.
- `.env`: OpenAI API 키를 저장하는 환경 변수 파일입니다.

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 만듭니다.
```sh
git checkout -b feature/your-feature-name
```
3. 변경 사항을 커밋합니다.
```sh
git commit -m 'Add some feature'
```
4. 브랜치에 푸시합니다.
```sh
git push origin feature/your-feature-name
```
5. Pull Request를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

## 연락처

프로젝트와 관련된 문의 사항이 있으시면 아래 이메일로 연락 주세요.
- Email: ai@soongsil.ac.kr
```

이 `README.md` 파일은 프로젝트에 대한 개요, 설치 방법, 사용 방법, 파일 설명, 기여 방법 및 라이선스 정보를 포함하고 있습니다. 필요에 따라 세부 사항을 조정하시면 됩니다.
