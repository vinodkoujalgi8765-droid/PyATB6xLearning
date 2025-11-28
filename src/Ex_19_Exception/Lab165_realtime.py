import requests

user_url = input("Enter the url ")
try:
    response = requests.get(user_url)
    print(response.status_code)
except requests.exceptions.MissingSchema:
    print("Invalid URL ")
except Exception as e:
    print(e)


