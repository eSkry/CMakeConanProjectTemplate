import os
import subprocess
import platform
import sys


def shell_command(directory, program, args=None, no_errors=False):
    if args is None:
        args = []
    if isinstance(args, str):
        args = [args]

    if platform.system().lower() == "linux":
        args = [f'"{arg}"' for arg in args]
    args.insert(0, program)

    old_dir = os.getcwd()
    os.chdir(old_dir)

    ret_code = subprocess.call(args, stderr=subprocess.STDOUT, shell=True)

    os.chdir(old_dir)
    if ret_code and no_errors:
        raise Exception(f"Execute shell command error: ({program}): {ret_code}")
    return ret_code


def shell_command_ret(directory, program, args=None):
    if args is None:
        args = []
    if isinstance(args, str):
        args = [args]

    if platform.system().lower() == "linux":
        args = [f'"{arg}"' for arg in args]
    args.insert(0, program)

    old_dir = os.getcwd()
    os.chdir(old_dir)

    result_data = {"stdout": "", "stderr": ""}

    popen = subprocess.Popen(" ".join(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = popen.communicate()
    popen.wait()
    result_data['stdout'] = stdout.strip().decode('utf-8', errors='ignore')
    result_data['stderr'] = stderr.strip().decode('utf-8', errors='ignore')

    os.chdir(old_dir)

    return result_data
