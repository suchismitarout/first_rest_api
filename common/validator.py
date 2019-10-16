def validate_id(id):
    try:
        if not id.isnumeric():
            raise ValueError("enter in proper format")
    except ValueError as e:
        print("error", e)


def validate_age(age):
    try:
        if not age.isdigit():
            raise ValueError("enter in correct format")
    except ValueError as e:
        print("error", e)


