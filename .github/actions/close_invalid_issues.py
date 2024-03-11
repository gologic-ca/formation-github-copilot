from github import Githubs
import os

# First create a Github instance:

g = Github(os.getenv('GITHUB_TOKEN'))

# Then play with your Github objects:
for issue in g.get_repo(os.getenv('GITHUB_REPOSITORY')).get_issues(state='open'):
  if any(label.name == 'invalid' for label in issue.get_labels()):
    issue.edit(state='closed')
    print(f'Closed issue {issue.number}')
