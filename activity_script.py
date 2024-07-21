import requests
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

# Replace with your GitHub username
username = "4rivappa"

# Define the date range for fetching data
start_date = "2023-01-01"  # Start date for fetching data
end_date = str(datetime.date.today())  # End date for fetching data (today's date)

# Function to fetch GitHub activity data with pagination handling
def fetch_github_activity(username):
    # Base URL for fetching user events from GitHub API
    url = f"https://api.github.com/users/{username}/events"
    
    # Headers to set the user-agent
    headers = {
        'User-Agent': 'request'
    }
    
    # Initialize the list to store all events
    all_events = []
    
    # Loop to handle pagination
    while url:
        # Make the GET request to the GitHub API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.status_code}")
        
        # Extend the list with the new events
        all_events.extend(response.json())
        
        # Check if there is a 'Link' header for pagination
        links = response.headers.get('Link')
        if links:
            # Extract the next page URL from the 'Link' header
            next_url = None
            for link in links.split(','):
                if 'rel="next"' in link:
                    next_url = link.split(';')[0].strip('<> ')
                    break
            url = next_url
        else:
            break
    
    return all_events

# Fetch the data using the function
activity_data = fetch_github_activity(username)

# Process the data to extract and aggregate relevant information
activity_counts = defaultdict(int)

for event in activity_data:
    # Extract the date from the event timestamp (first 10 characters of 'created_at')
    date = event['created_at'][:10]
    # Increment the activity count for the date
    activity_counts[date] += 1

# Sort the dates and counts
sorted_dates = sorted(activity_counts.keys())
sorted_counts = [activity_counts[date] for date in sorted_dates]

# Plot the graph using matplotlib
plt.figure(figsize=(10, 5))  # Create a new figure with specified size
plt.plot(sorted_dates, sorted_counts, marker='o')  # Plot the data with dates on x-axis and counts on y-axis
plt.title('GitHub Activity Over Time')  # Set the title of the graph
plt.xlabel('Date')  # Label the x-axis
plt.ylabel('Activity Count')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit elements properly
plt.savefig('activity_graph.png')  # Save the graph as an image file

print("Graph generated and saved as activity_graph.png")  # Print confirmation message
