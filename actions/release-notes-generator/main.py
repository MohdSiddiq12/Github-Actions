import os
import github

def run():
    try:
        latest_tag = os.getenv('INPUT_LATEST-TAG')
        g = github.Github(os.getenv('GITHUB_TOKEN'))
        repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
        
        # Fetch the commit history between the latest tag and the current commit
        commits = repo.compare(latest_tag, 'HEAD').commits
        
        changelog = ''
        for commit in commits:
            changelog += f'- {commit.commit.message}\n'
        
        print(f'::set-output name=changelog::{changelog}')
    except Exception as e:
        print(f'::error::{e}')
        exit(1)

if __name__ == '__main__':
    run()
