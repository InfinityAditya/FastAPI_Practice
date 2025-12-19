from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
import sklearn

# --- Fix for scikit-learn pickle compatibility ---
import sklearn.compose._column_transformer as ct
class _RemainderColsList(list):
    pass
ct._RemainderColsList = _RemainderColsList

# --- Load trained model ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- FastAPI app ---
app = FastAPI()

# City categories
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# --- Input Schema ---
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user (kg)")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user (meters)")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Annual salary of the user in LPA")]
    smoker: Annotated[bool, Field(..., description="Is user a smoker?")]
    city: Annotated[str, Field(..., description="City that the user belongs to")]
    occupation: Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job',
                'business_owner', 'unemployed', 'private_job'],
        Field(..., description="Occupation of the user")
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

# --- API Route ---
@app.post("/predict")
def predict_premium_label(data: UserInput):
    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predicted_category": prediction})
