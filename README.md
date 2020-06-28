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
	Data : Google Drive
  
## - 디렉토리 구조
### NSMC
    - Data : 학습 데이터, 테스트 데이터가 있는 디렉토리
    - Models : 학습된 모델이 저장되는 디렉토리
    - result : 학습된 모델이 예측한 결과를 저장하는 디렉토리
### Friends
    - Data : 학습 데이터, 테스트 데이터가 있는 디렉토리
    - Preprocess : 전처리하는 코드와 원래 데이터가 포함된 디렉토리
        - data/preprocess_data : 전처리 결과
        - data/Friends : 전처리 이전
    - model_save : 학습된 모델이 저장되는 디렉토리, BERT의 모델이 여기에 저장되며 LSTM은 Friends에 저장된다.

## - How to execute
- Before execution
  - NSMC
    - Nope
  - Friends
    - Preprocessing (Output 파일 이미 존재 - /preprocess/data/preprocess_data/*), 로컬 환경에서 디렉토리에 들어가 실행해야 함.
    <pre>
    python data_preprocess.py
    </pre>
    - Convert Preprocessed data to CSV (수작업, Output 파일 이미 존재 - /data/*)
    - en_data Preprocessing (수작업, 이미 논문에 언급한대로 전처리 완료 - /data/en_data.csv)

- Execution
  1. Google Drive root에 NLP_Term 디렉토리 생성 후 각각의 폴더 /NLP_Term/ 에 업로드 (경로수정 필요할 시 ipynb의 디렉토리 경로 수정, 하단에 표시.)
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
  3. 맨 위부터 순서대로 실행

## - 참고자료
- 참고한 코드
  - https://github.com/yashsharan/Multi-Class-sentiment-analysis
  - https://github.com/lkluo/emotionX-2018/tree/master/dataset
  - https://colab.research.google.com/drive/1tIf0Ugdqg4qT7gcxia3tL7und64Rv1dP
  
- 참고 논문
  - https://www.aclweb.org/anthology/L18-1252.pdf