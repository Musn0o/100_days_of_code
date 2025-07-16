import requests
from datetime import datetime

# --- Configuration ---
# Your Pixela username
PIXELA_USERNAME = "YOUR_PIXELA_USERNAME"
# Your Pixela personal token (keep this secret!)
PIXELA_TOKEN = "YOUR_PIXELA_TOKEN"
# The ID for your habit graph (e.g., "coding-graph", "exercise-tracker")
GRAPH_ID = "YOUR_GRAPH_ID"

# Pixela API endpoints
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# --- 1. Create User Account (Run once) ---
# You only need to run this code once to create your Pixela account.
# After successful creation, you can comment it out.
user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# print("Creating Pixela user...")
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# --- 2. Create a Graph (Run once per graph) ---
# You only need to run this code once per graph you want to create.
# After successful creation, you can comment it out.
graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Progress Graph",
    "unit": "hour", # Or "commit", "km", "pages", etc.
    "type": "float", # Or "int"
    "color": "ajisai", # Available colors: shibafu, momiji, sora, ichou, ajisai, kuro
}

# Headers for authentication (required for graph creation and pixel operations)
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# print("\nCreating Pixela graph...")
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --- 3. Post a Pixel (Add a value to the graph for a specific date) ---
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

# Get today's date in YYYYMMDD format
today = datetime.now()
# For a specific date, you could use:
# today = datetime(year=2023, month=7, day=21)

pixel_data = {
    "date": today.strftime("%Y%m%d"), # Format date as YYYYMMDD
    "quantity": "2.5", # Quantity of your habit (e.g., hours coded, km run)
}

print(f"\nPosting pixel for {today.strftime('%Y-%m-%d')} with quantity {pixel_data['quantity']}...")
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# --- 4. Update a Pixel (Modify an existing pixel's value) ---
# You need to specify the date of the pixel you want to update.
update_date = today.strftime("%Y%m%d") # Update today's pixel
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{update_date}"

new_pixel_data = {
    "quantity": "3.0", # New quantity value
}

print(f"\nUpdating pixel for {update_date} to quantity {new_pixel_data['quantity']}...")
response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# --- 5. Delete a Pixel (Remove a pixel for a specific date) ---
# You need to specify the date of the pixel you want to delete.
delete_date = today.strftime("%Y%m%d") # Delete today's pixel
pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

print(f"\nDeleting pixel for {delete_date}...")
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)

# --- View Your Graph ---
# After running, you can view your graph in a web browser at:
# https://pixe.la/v1/users/YOUR_PIXELA_USERNAME/graphs/YOUR_GRAPH_ID.html
# Replace YOUR_PIXELA_USERNAME and YOUR_GRAPH_ID with your actual values.
print(f"\nCheck your graph at: https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}.html")

