import http.client
import json

URL = "20.244.56.144"
PATH = "/test/auth"

connection = http.client.HTTPConnection(URL)

data = {
    "companyName":"goMart","clientID":"ee794832-f103-4b72-85c2-d0ac57892f8f","clientSecret":"lGmxPKnNRlfyEtrD","ownerName":"sahana","ownerEmail":"new-email@example.com","rollNo":"4SO22CS408"
}

json_data = json.dumps(data)

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    connection.request("POST", PATH, body=json_data, headers=headers)

    response = connection.getresponse()
    response_data = response.read()

    if response.status == 409:
        print("Registration failed: Email is already registered.")
        # Handle additional logic or inform the user as needed

    else:
        print("Status:", response.status)
        print("Response:", response_data.decode())

except http.client.HTTPException as e:
    print(f"HTTPException occurred: {e}")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    connection.close()
