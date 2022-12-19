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
    def testIDIsString(self):
        # test to see if the input GitHub ID is a string
        ID = "cconway1-stevens"
        self.assertIs(type(ID), str)
    def testOutput(self):
        # test to see if the output of the given ID is correct
        output = ['Error getting commits for repository cconway1-stevens: 409',
          'Error getting commits for repository personalsite: 409',
          'Error getting commits for repository test-HW3: 409',
          'Repo: Complexity Number of commits: 30',
          'Repo: Complexity-1 Number of commits: 30',
          'Repo: E_115-Final Number of commits: 1',
          'Repo: HW_SSW345 Number of commits: 2',
          'Repo: SSW345 Number of commits: 12',
          'Repo: SSW567-HW4a Number of commits: 2',
          'Repo: SSW_567 Number of commits: 28',
          'Repo: stevens-ssw-567-Final Number of commits: 13',
          'Repo: Testsite Number of commits: 1']

        self.assertEqual(github_user("cconway1-stevens"), output)

    def testRepoError(self):
        # test to see if the repository exists for given ID
        ID = "asdasdasdasd"
        self.assertEqual(github_user(ID), "Error obtaining repository names!")
    def testCommitError(self):
        # test to see if the commits exist in the repository for given ID
        self.assertEqual(github_user("SSWSample"), "Error obtaining number of commits!")
        self.assertEqual(github_user("cconway1-stevens"), ['Error getting commits for repository cconway1-stevens: 409',
          'Error getting commits for repository personalsite: 409',
          'Error getting commits for repository test-HW3: 409',
          'Repo: Complexity Number of commits: 30',
          'Repo: Complexity-1 Number of commits: 30',
          'Repo: E_115-Final Number of commits: 1',
          'Repo: HW_SSW345 Number of commits: 2',
          'Repo: SSW345 Number of commits: 12',
          'Repo: SSW567-HW4a Number of commits: 2',
          'Repo: SSW_567 Number of commits: 28',
          'Repo: stevens-ssw-567-Final Number of commits: 13',
          'Repo: Testsite Number of commits: 1'])

