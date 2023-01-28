import os
import shell_command


def has_git(directory):
    """Check directory .git exists"""
    return os.path.exists(os.path.join(directory, ".git"))


def git_add(directory, files=None):
    """Run command 'git add <files>'"""
    if files is None:
        files = []
    if isinstance(files, str):
        files = [files]

    for file in files:
        shell_command.shell_command_in_dir(directory, "git", ["add", file])


def git_commit(directory, message):
    """Run command 'git commit -m <message>'"""
    shell_command.shell_command_in_dir(directory, "git", ["commit", "-m", f'"{message}"'])


def git_fetch_and_pull(directory):
    """Run command 'git fetch' and 'git pull'"""
    shell_command.shell_command_in_dir(directory, "git", ["fetch"])
    shell_command.shell_command_in_dir(directory, "git", ["pull"])


def git_checkout(directory, branch):
    """Run command 'git checkout <branch>'"""
    shell_command.shell_command_in_dir(directory, "git", ["checkout", branch])


def git_create_branch(directory, branch):
    """Run command 'git checkout -b <branch>'"""
    shell_command.shell_command_in_dir(directory, "git", ["checkout", "-b", branch])


class SimpleGit:
    def __int__(self, directory):
        self._directory = directory
        if not has_git(self._directory):
            raise Exception(f"Folder {directory} is not git repository!")

    def pull(self):
        git_fetch_and_pull(self._directory)

    def commit(self, message):
        git_commit(self._directory, message)

    def add(self, files=None):
        git_add(self._directory, files)

    def checkout(self, branch):
        git_checkout(self._directory, branch)

    def create_branch(self, branch):
        git_create_branch(self._directory, branch)
