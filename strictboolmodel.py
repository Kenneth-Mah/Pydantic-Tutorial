from pydantic import BaseModel, StrictBool, ValidationError

class StrictBoolModel(BaseModel):
    strict_bool: StrictBool

data = {
    'strict_bool': False
}

try:
    strictboolmodel = StrictBoolModel(**data)

    print(strictboolmodel)
except ValidationError as e:
    print(e.json())