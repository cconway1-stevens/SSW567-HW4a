import requests
import json
import unittest
from GitHubAPI1 import get_repos_and_commits
def get_repos_and_commits(github_id):
    # Make the API call to get the list of repositories for the given GitHub ID
    repos_url = f"https://api.github.com/users/{github_id}/repos"
    repos_response = requests.get(repos_url)

    # If the API call was successful, parse the list of repositories
    if repos_response.status_code == 200:
        repos_data = json.loads(repos_response.text)
        result = []

        # For each repository, make an API call to get the list of commits
        for repo in repos_data:
            repo_name = repo['name']
            commits_url = f"https://api.github.com/repos/{github_id}/{repo_name}/commits"
            commits_response = requests.get(commits_url)

            # If the API call was successful, parse the list of commits
            if commits_response.status_code == 200:
                commits_data = json.loads(commits_response.text)
                result.append((repo_name, len(commits_data)))
            else:
                print(f"Error getting commits for repository {repo_name}: {commits_response.status_code}")

        return result
    else:
        print(f"Error getting repositories: {repos_response.status_code}")
        return None

# Example usage
github_id = "cconway1-stevens"
repos_and_commits = get_repos_and_commits(github_id)

if repos_and_commits is not None:
    for repo_name, commit_count in repos_and_commits:
        print(f"Repo: {repo_name} Number of commits: {commit_count}")

# create unit test cases for the above functions
# Path: GitHubAPI1_test.py

class TestGitHubAPI1(unittest.TestCase):
    def test_get_repos_and_commits(self):
        github_id = "cconway1-stevens"
        repos_and_commits = get_repos_and_commits(github_id)
        self.assertEqual(len(repos_and_commits), 1)
        self.assertEqual(repos_and_commits[0][0], "GitHubAPI1")
        self.assertEqual(repos_and_commits[0][1], 1)

