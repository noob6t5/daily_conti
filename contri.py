import requests
import random
import time
from datetime import datetime
import base64

# Configuration
GITHUB_TOKEN = (
    ""  # Replace with your GitHub PAT
) 
REPO_OWNER = ''  # Your GitHub username
REPO_NAME = ''      # Your private repo name
FILE_PATH = 'README.md'
BASE_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_file_info():
    response = requests.get(BASE_URL, headers=headers)
    response.raise_for_status()
    return response.json()

def update_readme(content, sha):
    updated_content = {
        'message': f'Random edit {datetime.now()}',
        'content': base64.b64encode(content.encode()).decode(),  # Encode content in base64
        'sha': sha
    }
    response = requests.put(BASE_URL, headers=headers, json=updated_content)
    response.raise_for_status()
    print(f'Updated README.md: {updated_content["message"]}')

def main():
    # Get the initial README.md content and SHA
    file_info = get_file_info()
    sha = file_info['sha']
    content = base64.b64decode(file_info['content']).decode()  # Decode the existing content

    # Randomly determine the number of changes (between 1 and 10)
    num_changes = random.randint(1, 10)
    print(f'Making {num_changes} random changes to README.md.')

    # Make the specified number of changes
    for i in range(num_changes):
        # Randomly edit the content
        random_line = f'Random edit {i+1} on {datetime.now()} - {random.randint(1, 100)}\n'
        updated_content = content + random_line

        # Update the README.md file
        update_readme(updated_content, sha)

        # Refresh the SHA for the next update
        file_info = get_file_info()  # Fetch the updated file info again
        sha = file_info['sha']  # Update SHA for the next commit
        content = base64.b64decode(file_info['content']).decode()  # Decode the updated content

        time.sleep(1)  # Sleep for a second to avoid rate limits (optional)

if __name__ == "__main__":
    main()
