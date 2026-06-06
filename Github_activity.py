import sys
import json
import urllib.request
import urllib.error


def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Python-CLI-app')

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for event in data:
                display_activity(data)
    
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"User '{username}' not found.")
        elif e.code == 403:
            print("Access forbidden. Please check your API token.")
        else:
            print(f"HTTP Error: {e.code}")
    except Exception as e:
        print(f"An error occurred: {e}.Check your internet connection and try again.")

def display_activity(events):
    if not events:
        print("No events found for this user.")
        return
    print("\nOutput:")
    for event in events[:10]:
        event_type = event.get('type', 'N/A')
        repo_name = event.get('repo', {}).get('name', 'N/A')

        if event_type == 'PushEvent':
            commits = event.get('payload', {}).get('commits', [])
            commit_messages = [commit.get('message', 'N/A') for commit in commits]
            print(f"Event Type: {event_type}, Repository: {repo_name}, Commits: {', '.join(commit_messages)}")
        elif event_type == 'IssueEvent':
            issue_title = event.get('payload', {}).get('issue', {}).get('title', 'N/A')
            print(f"Event Type: {event_type}, Repository: {repo_name}, Issue: {issue_title}")
        
        elif event_type == 'WatchEvent':
            print(f"Event Type: {event_type}, Repository: {repo_name}, Action: {event.get('payload', {}).get('action', 'N/A')}")
        
        elif event_type == 'CreateEvent':
            print(f"Event Type: {event_type}, Repository: {repo_name}, Ref Type: {event.get('payload', {}).get('ref_type', 'N/A')}")

        else:
            # Fallback for event types we haven't explicitly mapped
            # Strips 'Event' from 'ForkEvent' to show 'Fork'
            clean_name = event_type.replace('Event', '') if event_type else "Activity"
            print(f"- Performed {clean_name} action in {repo_name}")