import requests

# This loop will count from 1 to 100
for count in range(1, 101):
    # Print the current count
    print(count)

# Send a GET request to Google.com
response = requests.get("https://www.google.com")

# Print the status code of the response
print("Response status code:", response.status_code)