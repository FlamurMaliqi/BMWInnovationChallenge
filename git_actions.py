from git import Repo

# The path to the repository
path = '~/BMW_dir/G_00.20_9xx_Musterordner_Dokum._2.3'


def git_init(repo_dir):
    """
    Initialize a new git repository at the given directory.

    Parameters:
    repo_dir (str): The directory where the repository should be initialized.
    """
    Repo.init(repo_dir)


def git_add(repo_dir):
    """
    Add all changes in the given repository to the staging area.

    Parameters:
    repo_dir (str): The directory of the repository.
    """
    repo = Repo(repo_dir)
    repo.index.add('*')


def git_commit(repo_dir, commit_message):
    """
    Commit all changes in the staging area with the given message.

    Parameters:
    repo_dir (str): The directory of the repository.
    commit_message (str): The message for the commit.
    """
    repo = Repo(repo_dir)
    repo.index.commit(commit_message)


def accept_changes(repo_dir, message):
    """
    Add all changes to the staging area and commit them with the given message.

    Parameters:
    repo_dir (str): The directory of the repository.
    message (str): The message for the commit.
    """
    git_add(repo_dir)
    git_commit(repo_dir, message)


def git_status(repo_dir):
    """
    Get the status of the repository.

    Parameters:
    repo_dir (str): The directory of the repository.

    Returns:
    dict: A dictionary where the keys are the file paths and the values are the status codes.
    """
    repo = Repo(repo_dir)
    status_output = repo.git.status('--porcelain')
    lines = status_output.split('\n')
    status_dict = {}
    for line in lines:
        if line:
            status_code, file_path = line.split(maxsplit=1)
            status_dict[file_path] = status_code
    return status_dict


def git_diff(repo_dir, file_path):
    """
    Perform a git diff on a specific file in the given repository.

    Parameters:
    repo_dir (str): The directory of the repository.
    file_path (str): The path to the file to diff, relative to the repository root.

    Returns:
    str: The output of the git diff command.
    """
    repo = Repo(repo_dir)
    diff_index = repo.index.diff(None)
    diffs = diff_index.iter_change_type('M')
    #diffs = [d for d in diff_index.iter_change_type('M') if d.a_path == file_path or d.b_path == file_path]
    #assert diffs.__len__() == 1
    return diffs


def format_diff(diff):
    """
    Format a Diff object into a human-readable string.

    Parameters:
    diff (git.Diff): The Diff object to format.

    Returns:
    str: A string describing the changes.
    """
    lines = []
    if diff.renamed_file:
        lines.append(f"File renamed from {diff.a_path} to {diff.b_path}")
    else:
        lines.append(f"Changes to file {diff.a_path}")

    for line in diff.diff.splitlines():
        if line.startswith('-'):
            lines.append(f"Removed: {line[1:]}")
        elif line.startswith('+'):
            lines.append(f"Added: {line[1:]}")

    return '\n'.join(lines)


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
    diff = git_diff('.', 'process_excel.py')
    for i in diff:
        print(format_diff(i))