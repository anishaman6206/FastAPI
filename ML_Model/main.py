from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_predictions 
from typing import List

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Welcome to the House Price Prediction API!'}


# user will send data, since we will receive data and return a prediction, we will use post method
@app.post('/prediction', response_model=OutputSchema) # response_model is used to define the structure of the response
def predict_price(user_input: InputSchema):
    input_dict = user_input.model_dump()  # convert pydantic model to dictionary
    prediction = make_prediction(input_dict)  # call the function from predict.py
    return OutputSchema(median_house_value=round(prediction, 2))  # return the prediction in the response model


@app.post('/batch_prediction', response_model = List[OutputSchema])
def batch_prediction(user_input: List[InputSchema]) -> List[OutputSchema]:
    predictions = make_batch_predictions([x.model_dump() for x in user_input])
    return [OutputSchema(median_house_value=round(pred, 2)) for pred in predictions]
