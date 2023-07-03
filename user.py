from datetime import datetime
from typing import List, Optional

from pydantic_core.core_schema import FieldValidationInfo

from pydantic import BaseModel, ValidationError, field_validator

class User(BaseModel):
    id: int
    username: str
    password: str
    confirm_password: str
    alias: str = 'anonymous'
    timestamp: Optional[datetime] = None
    friends: List[int] = []

    @field_validator('id')
    def id_must_be_4_digits(cls, v):
        if len(str(v)) != 4:
            raise ValueError('must be 4 digits')
        return v
    
    @field_validator('confirm_password')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('passwords do not match')
        return v

data = {
    'id': '1234', 
    'username': 'wai foong', 
    'password': 'Password123', 
    'confirm_password': 'Password123', 
    'timestamp': '2020-08-03 10:30', 
    'friends': [1, '2', b'3']
}

try:
    user = User(**data)

    print(user)
except ValidationError as e:
    print(e.json())
