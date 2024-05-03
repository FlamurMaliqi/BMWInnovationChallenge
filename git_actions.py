from git import Repo

path = '~/BMW_dir/G_00.20_9xx_Musterordner_Dokum._2.3'


def git_init(repo_dir):
    Repo.init(repo_dir)


def git_add(repo_dir):
    repo = Repo(repo_dir)
    repo.index.add('*')


def git_commit(repo_dir, commit_message):
    repo = Repo(repo_dir)
    repo.index.commit(commit_message)


def git_status(repo_dir):
    repo = Repo(repo_dir)
    return repo.git.status()


if __name__ == '__main__':
    git_add('.')
    print(git_status('.'))
