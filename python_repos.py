import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code {r.status_code}")

# Store the API response in a varibable.
response_dict = r.json()

# Explore information about the repositories.
repo_dicts = response_dict['items']

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nPrint selected information about each repository.")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository.")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")