import os
from scripts import shell


def has_git(directory):
    """Check directory .git exists"""
    return os.path.exists(os.path.join(directory, ".git"))


def add(directory, files=None):
    """Run command 'git add <files>'"""
    if files is None:
        files = []
    if isinstance(files, str):
        files = [files]

    for file in files:
        shell.command_in_dir(directory, "git", ["add", file])


def commit(directory, message):
    """Run command 'git commit -m <message>'"""
    shell.command_in_dir(directory, "git", ["commit", "-m", f'"{message}"'])


def fetch_and_pull(directory):
    """Run command 'git fetch' and 'git pull'"""
    shell.command_in_dir(directory, "git", ["fetch"])
    shell.command_in_dir(directory, "git", ["pull"])


def checkout(directory, branch):
    """Run command 'git checkout <branch>'"""
    shell.command_in_dir(directory, "git", ["checkout", branch])


def create_branch(directory, branch):
    """Run command 'git checkout -b <branch>'"""
    shell.command_in_dir(directory, "git", ["checkout", "-b", branch])


def clone(directory, url):
    """Run command 'git clone <url>'"""
    shell.command_in_dir(directory, "git", ["clone", url])


def commit_hash(directory):
    """Run command 'git rev-parse HEAD'"""
    res = shell.command_ret_in_dir(directory, "git", ["rev-parse", "HEAD"])
    if res['stdout']:
        return res['stdout']
    return None


def tag(directory, tag_name, tag_message):
    """Run command 'git tag -a <tag_name> -m <tag_message>'"""
    shell.command_in_dir(directory, "git", ["tag", "-a", tag_name, "-m", tag_message])


def list_branch(directory):
    """Run command 'git branch -a'"""
    res = shell.command_ret_in_dir(directory, "git", ["branch", "-a"])
    ret_value = []

    if res['stdout']:
        split_list = res['stdout'].split('\n')
        for branch in split_list:
            ret_value.append(branch.replace('\r', '').replace('*', '').strip())

    return ret_value


def current_branch(directory):
    """Run command 'git branch -a' and find branch with *"""
    res = shell.command_ret_in_dir(directory, "git", ["branch", "-a"])

    if res['stdout']:
        split_list = res['stdout'].split('\n')
        for branch in split_list:
            if branch.startswith('*'):
                return branch.replace('*', '').replace('\r', '').strip()

    return None


def init(directory):
    """Run command 'git init'"""
    shell.command_in_dir(directory, "git", ["init"])


class SimpleGit:
    def __int__(self, directory, init_repo_if_not_exists=False):
        self._directory = directory
        if not has_git(self._directory) and not init_repo_if_not_exists:
            raise Exception(f"Folder {directory} is not git repository!")
        elif not has_git(self._directory):
            init(self._directory)

    def pull(self):
        fetch_and_pull(self._directory)

    def commit(self, message):
        commit(self._directory, message)

    def add(self, files=None):
        add(self._directory, files)

    def checkout(self, branch):
        checkout(self._directory, branch)

    def create_branch(self, branch):
        create_branch(self._directory, branch)

    def hash(self):
        return commit_hash(self._directory)

    def tag(self, tag_name, tag_message):
        tag(self._directory, tag_name, tag_message)

    def branch_list(self):
        return list_branch(self._directory)

    def current_branch(self):
        return current_branch(self._directory)
