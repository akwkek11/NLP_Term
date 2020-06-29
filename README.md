NLP Term Project Repository (2020, Korea University, 11조)
======================

## - 팀원
- 주어진
- 이강빈
- 홍선우

## - 환경
### NSMC
	Code : Google Colab
	Data : Google Drive
### Friends
	Code : Google Colab
	Data : Google Drive ( Preprocessing : Local, Python 3.7 )
  
## - 디렉토리 구조
### NSMC
    - root : /NLP_Term/NSMC/

    - Data : 학습 데이터, 테스트 데이터가 있는 디렉토리
    - Models : 학습된 모델이 저장되는 디렉토리
    - result : 학습된 모델이 예측한 결과를 저장하는 디렉토리
### Friends
    - root : /NLP_Term/Friends/

    - Data : 학습 데이터, 테스트 데이터가 있는 디렉토리
    - Preprocess : 전처리하는 코드와 원래 데이터가 포함된 디렉토리
        - data/preprocess_data : 전처리 결과
        - data/Friends : 전처리 이전
    - model_save : 학습된 모델이 저장되는 디렉토리, BERT의 모델이 여기에 저장되며 LSTM은 Friends에 저장됩니다.

## - How to execute
- Before execution
  - NSMC
    - Nope
  - Friends
    - Preprocessing (Output 파일 이미 존재 - /preprocess/data/preprocess_data/*), 만약 실행이 필요할 시, 로컬 환경에서 디렉토리에 접근하여 실행해야 합니다.
    <pre>
    python data_preprocess.py
    </pre>
    - Convert Preprocessed data to CSV (수작업, Output 파일 이미 존재 - /data/*)
    - en_data Preprocessing (수작업, 이미 논문에 언급한대로 전처리 완료 - /data/en_data.csv)

- Execution
  1. Google Drive root에 NLP_Term 디렉토리 생성 후 각각의 폴더를 /NLP_Term/ 에 업로드합니다. (경로수정 필요할 시 ipynb의 디렉토리 경로 수정, 하단에 표시.)
  <pre>
    drive.mount('/content/gdrive/')
    ...
    train_data = pd.read_table('/content/gdrive/My Drive/NLP_Term/NSMC/Data/ratings_train.txt')
    test_data = pd.read_table('/content/gdrive/My Drive/NLP_Term/NSMC/Data/ratings_test.txt')
    stop_word = pd.read_table('/content/gdrive/My Drive/NLP_Term/NSMC/Data/stopword.txt')
    ...
    model.save("/content/gdrive/My Drive/NLP_Term/NSMC/Models/best_model" + str(model_num) + ".h5")
    ...
    score_data = pd.read_csv("/content/gdrive/My Drive/NLP_Term/NSMC/Data/ko_data.csv", encoding='cp949')
    ...
    loaded_model = load_model("/content/gdrive/My Drive/NLP_Term/NSMC/Models/best_model" + str(model_num) + ".h5")
    ...
    new_df.to_csv("/content/gdrive/My Drive/NLP_Term/NSMC/result/solution" + str(i) + ".csv", index=False)
    ...
    os.chdir('gdrive/My Drive/NLP_Term/Friends')
    ...  
    os.chdir('/content/gdrive/My Drive/NLP_Term/Friends')
  </pre>
  2. NLP_Term.ipynb 구글 드라이브에 업로드 이후 Colab으로 열기
  3. ipynb 코드 맨 위부터 순서대로 실행
  <pre>
    1. 런타임 -> 런타임 유형 변경 'GPU' 설정 필요합니다.
    2. Google Drive Mount이전에 Data를 전부 업로드해야 합니다.
    3. 중간부터 실행이 불가능하므로 Mount Drive부분은 먼저 꼭 실행해줘야 합니다.
  </pre>

## - 참고자료
- 참고한 자료/코드
  - NSMC
    - https://wikidocs.net/44249
    - https://bab2min.tistory.com/544 
  - Friends
    - https://github.com/yashsharan/Multi-Class-sentiment-analysis
    - https://github.com/lkluo/emotionX-2018/tree/master/dataset
    - https://colab.research.google.com/drive/1tIf0Ugdqg4qT7gcxia3tL7und64Rv1dP
  
- 참고 논문
  - https://www.aclweb.org/anthology/L18-1252.pdf

- 데이터 업로드/Colab URL
  - Google Colab : https://colab.research.google.com/drive/1AWK3ETqwIJkL7hQH58SIHelvRETEBJmD#scrollTo=IQ2rrkIVEnIx
  - Google Drive : https://drive.google.com/drive/folders/11TCXaC0lKjXzGJYhmNu6ZobyzZT8-qD7