import os
from scripts import shell_command


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


def git_clone(directory, url):
    """Run command 'git clone <url>'"""
    shell_command.shell_command_in_dir(directory, "git", ["clone", url])


def git_commit_hash(directory):
    """Run command 'git rev-parse HEAD'"""
    res = shell_command.shell_command_ret_in_dir(directory, "git", ["rev-parse", "HEAD"])
    if res['stdout']:
        return res['stdout']
    return None


def git_tag(directory, tag_name, tag_message):
    """Run command 'git tag -a <tag_name> -m <tag_message>'"""
    shell_command.shell_command_in_dir(directory, "git", ["tag", "-a", tag_name, "-m", tag_message])


def git_list_branch(directory):
    """Run command 'git branch -a'"""
    res = shell_command.shell_command_ret_in_dir(directory, "git", ["branch", "-a"])
    ret_value = []

    if res['stdout']:
        split_list = res['stdout'].split('\n')
        for branch in split_list:
            ret_value.append(branch.replace('\r', '').replace('*', '').strip())

    return ret_value


def git_current_branch(directory):
    """Run command 'git branch -a' and find branch with *"""
    res = shell_command.shell_command_ret_in_dir(directory, "git", ["branch", "-a"])

    if res['stdout']:
        split_list = res['stdout'].split('\n')
        for branch in split_list:
            if branch.startswith('*'):
                return branch.replace('*', '').replace('\r', '').strip()

    return None


def git_init(directory):
    """Run command 'git init'"""
    shell_command.shell_command_in_dir(directory, "git", ["init"])


class SimpleGit:
    def __int__(self, directory, init_repo_if_not_exists=False):
        self._directory = directory
        if not has_git(self._directory) and not init_repo_if_not_exists:
            raise Exception(f"Folder {directory} is not git repository!")
        elif not has_git(self._directory):
            git_init(self._directory)

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

    def hash(self):
        return git_commit_hash(self._directory)

    def tag(self, tag_name, tag_message):
        git_tag(self._directory, tag_name, tag_message)

    def branch_list(self):
        return git_list_branch(self._directory)

    def current_branch(self):
        return git_current_branch(self._directory)
