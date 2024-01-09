## Setup Instructions

Before running the code, please set up your GitHub token:

1. Copy the `api.yml.template` file to a new file named `api.yml`.
2. Open `api.yml` and replace `PLACE_YOUR_TOKEN_HERE` with your GitHub personal access token.

Note: Do not upload `api.yml` to public repositories for security reasons.


To use the `github_user_info` function, follow the example below:

```python
user_obj = github_user_info('api.yml')

# Print some values
print('Username: ' + user_obj['login'])
print('Name: ' + user_obj['name'])
