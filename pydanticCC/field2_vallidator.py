from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List, Dict ,Optional

class Patient(BaseModel):

    name:str
    email: EmailStr
    age:int
    weight:float
    married:bool
    allergies: List[str]
    contact_details : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        value_domains=['hdfc.com', 'icici.com']
        # absc@gmail.com
        domain_name= value.split('@')[-1]

        if domain_name not in value_domains:
            raise ValueError('Not a valid email')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


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

patient_info = {'name':'Aditya','email':'pce123@icici.com','age':'30', 'weight':40.2 ,
                'married':False,'allergies':['pollen','dust'],'contact_details':{'phone':'298487364'}}

patient1= Patient(**patient_info) # validation -> type coeirson(if possible)

insert_patient_data(patient1)
update_patient_data(patient1) 