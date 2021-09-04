import uvicorn                          # importing Libraries
from fastapi import FastAPI
from CustomerInfo import CustomerInfo
import numpy as np
import pickle
import pandas as pd
                                        
app = FastAPI()                          #Creating  app object
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.get('/')                            # 3. Index route, opens automatically on http://127.0.0.1:8000
def index():
    return {'message': 'Hey Team, how are you doing today?'}

@app.post('/predict')                    # Lets Predict the customer segment
def predict_banknote(data:BankNote):     #    JSON data and return the predicted Bank Note with the confidence
    data = data.dict()                   # Order_Status_0','Order_Status_1','Days Before Last Trans','Avg Amount','Total Amount','Avg_Quantity
    Order_Status_0=data['Order_Status_0']
    Order_Status_1=data['Order_Status_1']
    Days_Before_Last_Trans=data['Days_Before_Last_Trans']
    Avg_Amount=data['Avg_Amount']
    Total_Amount=data['Total_Amount']
    Avg_Quantity=data['Avg_Quantity']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[Order_Status_0,Order_Status_1,Days_Before_Last_Trans,Avg_Amount,Total_Amount,Avg_Quantity]])
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
