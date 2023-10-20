import requests

# This loop will count from 1 to 100
for count in range(1, 101):
    # Print the current count
    print(count)

# Send a GET request to Google.com
response = requests.get("https://www.google.com")

# Check if the response status code is 404
if response.status_code == 404:
    print("Error 404: Page not found")
else:
    # Print the status code and headers of the response
    print("Response status code:", response.status_code)
    print("Response headers:", response.headers)
    # Print the response body
    print("Response body:", response.text)