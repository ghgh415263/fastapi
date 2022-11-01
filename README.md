# fastapi로 딥러닝 모델 서버 구현
1. 파일을 받아서 224 x 224 x 3의 이미지로 전처리 한 후에 VGG16을 전이학습한 모델로 분류함
2. 모델의 학습은 Malimg 데이터셋을 사용하였다. (실제 악성코드를 수집하여 하진 않고 학술용 데이터셋을 사용)
https://vision.ece.ucsb.edu/sites/default/files/publications/nataraj_vizsec_2011_paper.pdf

# 모델 구조
1. 특징추출계층은 VGG16 전이학습 (학습시 특징 추출계층의 마지막 레이어는 학습가능하게 설정)
2. 분류계층은 데이터셋의 클래스인 25개의 단일층 (DROPOUT을 0.7정도 넣으니 오버피팅이 많이 줄어서 넣어줌)

# fastapi 셋팅
1. 텐서플로우, fastapi, numpy 깔아라
2. 텐서플로우 모델은 모델세이브해서 올림 (model_path 변수에 저장)

# 결과값
1. 결과값은 json 형태로 날려야하니 파이썬 dict으로 만들어 날린다.
2. 각각의 클래스에 확률(소숫점 4자리까지)을 더해서 리스트로 만듬
