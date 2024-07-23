import requests
import matplotlib.pyplot as plt
import datetime

# Replace with your GitHub username
username = "jackvector634"  #your_github_username

# Define the date range for fetching data
start_date = "2023-01-01"  # Start date for fetching data
end_date = str(datetime.date.today())  # End date for fetching data (today's date)

# Function to fetch GitHub activity data
def fetch_github_activity(username, start_date, end_date):
    # URL for fetching user events from GitHub API
    url = f"https://api.github.com/users/{username}/events"
    
    # Parameters for the API request
    params = {
        'since': start_date,  # Start date for events
        'until': end_date     # End date for events
    }
    
    # Make the GET request to the GitHub API
    response = requests.get(url, params=params)
    
    # Return the JSON response
    return response.json()

# Fetch the data using the function
activity_data = fetch_github_activity(username, start_date, end_date)

# Process the data to extract relevant information
# (This part will involve parsing the JSON response and aggregating activity data)

# Initialize lists for dates and activity counts
dates = []  # List of dates
counts = []  # List of activity counts

# Example data processing (replace with actual processed data)
for event in activity_data:
    # Extract the date from the event timestamp (first 10 characters of 'created_at')
    date = event['created_at'][:10]
    
    # Add the date to the dates list
    dates.append(date)
    
    # Increment activity count (simplified example, each event is counted as 1)
    counts.append(1)

# Plot the graph using matplotlib
plt.figure(figsize=(10, 5))  # Create a new figure with specified size
plt.plot(dates, counts, marker='o')  # Plot the data with dates on x-axis and counts on y-axis
plt.title('GitHub Activity Over Time')  # Set the title of the graph
plt.xlabel('Date')  # Label the x-axis
plt.ylabel('Activity Count')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit elements properly
plt.savefig('activity_graph.png')  # Save the graph as an image file

print("Graph generated and saved as activity_graph.png")  # Print confirmation message