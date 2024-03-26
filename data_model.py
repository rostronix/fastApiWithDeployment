from pydantic import BaseModel
from typing import Optional

class InputDataModel(BaseModel):
	age: float
	sex: int
	cp: int
	trestbps: float
	chol: float
	fbs: float
	restecg: int
	thalach: float
	exang: int
	oldpeak: float
	slope: int
	ca: int
	thal: int
	
class OutputDataModel(BaseModel):
    predicted_value: bool
    predicted_class: str
