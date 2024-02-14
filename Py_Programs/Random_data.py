import requests

def get_user_info(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user_data = response.json()
    return user_data

user_id = int(input("Enter a user ID: "))
user_info = get_user_info(user_id)
print("User Information:")
print(f"Name: {user_info['name']}")
print(f"Email: {user_info['email']}")
