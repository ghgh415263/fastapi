# fastapi로 딥러닝 모델 서버 구현
매우 간단.


# fastapi 셋팅
1. 텐서플로우, fastapi, numpy 깔아라
2. 텐서플로우 모델은 모델세이브해서 올림 (model_path 변수에 저장)


# 구현
1. 파일을 parameter로 받는다.

2. 받은 파일을 이미지화한다. (224 x 224 x 3) -> 파일을 8비트씩 읽어서 색상값으로 만들면됨.
https://vision.ece.ucsb.edu/sites/default/files/publications/nataraj_vizsec_2011_paper.pdf
참고하면 좋다.

3. 결과값은 json 형태로 날려야하니 파이썬 dict으로 만들어 날린다.
