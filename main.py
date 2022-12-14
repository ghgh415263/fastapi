import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from io import BytesIO

from fastapi import FastAPI, File, UploadFile # FastAPI 모듈 가져오기

app = FastAPI() # 객체 생성

@app.get("/") # Route Path
def test_index():
	
    # Json 타입으로 값 반환
    return {
	    "Python": "Framework2",
	}
    
@app.post("/something")
def something(file: bytes = File()):
    class_list = ["c1", "c2", "c3", "c4", "c5",
                  "c6", "c7", "c8", "c9", "c10",
                  "c11", "c12", "c13", "c14", "c15",
                  "c16", "c17", "c18", "c19", "c20",
                  "c21", "c22", "c23", "c24", "c25"]
    K_BYTE = 1024
    model_path = './models/malwareClassification_cnnckpt'
    model = load_model(model_path)
    file_size = len(file)
    width = 0

    if file_size < (K_BYTE * 10):
        width = 32
    elif file_size < (K_BYTE * 30):
        width = 64
    elif file_size < (K_BYTE * 60):
        width = 128
    elif file_size < (K_BYTE * 100):
        width = 256
    elif file_size < (K_BYTE * 200):
        width = 384
    elif file_size < (K_BYTE * 500):
        width = 512
    elif file_size < (K_BYTE * 1000):
        width = 768
    else:
        width = 1024
    
    remain_pixel = file_size % width;
    file = file[:file_size-remain_pixel]
    file = np.frombuffer(file, dtype='uint8')
    image_array = file.reshape(-1,width)
    
    im = Image.fromarray(image_array).resize((224,224), Image.BILINEAR).convert("RGB")
    numpy_array = np.reshape(im,[1,224,224,3])

    predictions = model.predict(numpy_array)
    print(predictions[0])
    predictions = predictions[0].tolist()
    result = {}
    resultList = []
    for i in range(len(predictions)):
        predictions[i] = round(predictions[i],4)
        resultList.append(class_list[i]+": "+str(predictions[i]))
    result["apiName"] = "vgg16_model_v1"
    result["resultList"] = resultList
    
    print(result)
    return result
