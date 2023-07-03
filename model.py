from pydantic import (
    BaseModel,
    NegativeInt,
    PositiveInt,
    conint,
    conlist,
    constr,
    ValidationError
)

class Model(BaseModel):
    # minimum length of 2 and maximum length of 10
    short_str: constr(min_length=2, max_length=10)

    # pattern
    pattern_str: constr(pattern=r'^apple (pie|tart|sandwich)$')

    # remove whitespace from string
    strip_str: constr(strip_whitespace=True)

    # value must be greater than 1000 and less than 1024
    big_int: conint(gt=1000, lt=1024)
    
    # value is multiple of 5
    mod_int: conint(multiple_of=5)
    
    # must be a positive integer
    pos_int: PositiveInt
    
    # must be a negative integer
    neg_int: NegativeInt

    # list of integers that contains 1 to 4 items
    short_list: conlist(int, min_length=1, max_length=4)

data = {
    'short_str': 'a string',
    'pattern_str': 'apple sandwich',
    'strip_str': '5 blanks     ',
    'big_int': '1008',
    'mod_int': '555',
    'pos_int': '123',
    'neg_int': '-123',
    'short_list': ['1', '2', '3']
}

try:
    model = Model(**data)

    print(model)
except ValidationError as e:
    print(e.json())