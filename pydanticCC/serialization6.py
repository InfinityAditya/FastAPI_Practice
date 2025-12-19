# pydantic models exported in python dict, json file using serialization
# pydantic built in method fastapi to build api , dubbuging , login
from  pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin:str

class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address: Address


address_dict={'city':'nagpur','state':'maharashtra', 'pin':'440016'}

address1 = Address(**address_dict)

patient_dict ={'name':'shubham','gender':'Male','age':21,'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  #include and exclude 
print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))