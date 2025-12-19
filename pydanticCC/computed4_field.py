from pydantic import BaseModel , EmailStr , AnyUrl, computed_field
from typing import List, Dict ,Optional

class Patient(BaseModel):

    name:str
    email: EmailStr
    age:int
    weight:float # kg
    height:float # mtr
    married:bool
    allergies: List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight/self.height**2),2)
        return bmi

  


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
    print('BMI:',patient.bmi)
    print('updated')

patient_info = {'name':'Aditya','email':'pce123@gmail.com','age':70, 'weight':40.2,'height':1.8,'married':False,'allergies':['pollen','dust'],'contact_details':{'phone':'298487364','emergency':'121392873'}}

patient1= Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
