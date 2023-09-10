from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input
from models import Prediction_Output
import numpy as np

from tensorflow import keras

MODEL_PATH= 'pulsar_model.h5'
#Load TensorFlow Model
model = keras.models.load_model(MODEL_PATH)

router = APIRouter()

preds = []

@router.get("/ml")
def get_preds():
    return preds

@router.post("/ml",status_code=status.HTTP_201_CREATED, response_model=Prediction_Output)
def predict(pred_input: Prediction_Input):
    input_data = np.array([pred_input.Mean_DMSNR_Curve,pred_input.SD_DMSNR_Curve,pred_input.EK_DMSNR_Curve,pred_input.Skewness_DMSNR_Curve])
    prediction =  model.predict(input_data) 
    result = {"id": str(pred_input.id), "pred":prediction}
    preds.append(result)

    return result

    