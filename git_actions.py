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
    status_output = repo.git.status('--porcelain')
    lines = status_output.split('\n')
    status_dict = {}
    for line in lines:
        if line:
            status_code, file_path = line.split(maxsplit=1)
            status_dict[file_path] = status_code
    return status_dict


if __name__ == '__main__':
    '''
    Porcelain format:
        ' ' = unmodified
    
        M = modified
    
        T = file type changed (regular file, symbolic link or submodule)
    
        A = added
    
        D = deleted
    
        R = renamed
    
        C = copied (if config option status.renames is set to "copies")
    
        U = updated but unmerged
    '''
    print(git_status('.'))
