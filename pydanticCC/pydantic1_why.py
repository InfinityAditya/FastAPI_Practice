from pydantic import BaseModel , EmailStr , AnyUrl, Field
from typing import List, Dict ,Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give full name of Patient', example=['lal singh chaddha'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age:int = Field(gt=0, lt=120)
    weight:Annotated[float, Field(gt=0, strict=True)]
    married:Optional[bool] = None
    allergies: List[str]
    contact_details : Dict[str, str]



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
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

patient_info = {'name':'Aditya','email':'pce123@gmail.com',
                'linkedin_url':'https://linkedin.com/aditya' ,'age':30, 'weight':40.2 ,'allergies':['pollen','dust'],'contact_details':{'phone':'298487364'}}

patient1= Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)