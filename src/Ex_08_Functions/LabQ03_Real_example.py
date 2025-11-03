def validate_status_code(response_code):
    if response_code >0:
        if response_code == 200:
            return True
        else:
            return False
    else:
        return "it is negative"

result = validate_status_code(int(input("Enter response code: ")))
print(result)