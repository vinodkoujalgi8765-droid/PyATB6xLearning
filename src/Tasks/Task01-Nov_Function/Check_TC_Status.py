'''
Write a function check_status(status_code) that returns:

"PASS" if status_code = 200

"FAIL" if status_code = 400 or 500

"UNKNOWN" otherwise
'''
def check_status(status_code):
    if status_code <= 0:
        return "Only +ve numbers are allowed"

    if status_code == 200:
        return "PASS"
    elif status_code == 400 or status_code == 500:
        return "FAIL"
    else:
        return "UNKNOWN"


status_code1 = check_status(200)
status_code2 = check_status(400)
status_code3 = check_status(500)
status_code4 = check_status(600)
print(status_code4)
