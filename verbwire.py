import requests

api_key = "sk_live_0164b9b7-207f-453b-8bfc-4132f84448fb"
api_url = "https://api.verbwire.com/endpoint"

# Example request
params = {"param1": "value1", "param2": "value2"}
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(api_url, params=params, headers=headers)

# Handle response
if response.status_code == 200:
    data = response.json()
    # Process data as needed
else:
    print(f"Error: {response.status_code} - {response.text}")
