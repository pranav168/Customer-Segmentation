# -*- coding: utf-8 -*-

from pydantic import BaseModel

class CustomerInfo(BaseModel):
    Order_Status_0: float         
    Order_Status_1: float 
    Days Before Last Trans: float 
    Avg Amount: float
    Total Amount: float
    Avg_Quantity: float
