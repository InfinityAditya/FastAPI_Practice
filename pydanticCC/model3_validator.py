from pydantic import BaseModel , EmailStr , AnyUrl , Field, field_validator,model_validator
from typing import List, Dict ,Optional

class Patient(BaseModel):

    name:str
    email: EmailStr
    age:int
    weight:float
    married:bool
    allergies: List[str]
    contact_details : Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in  model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'Aditya','email':'pce123@gmail.com','age':70, 'weight':40.2,'married':False,'allergies':['pollen','dust'],'contact_details':{'phone':'298487364','emergency':'121392873'}}

patient1= Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)