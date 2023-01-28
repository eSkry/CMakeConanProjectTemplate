import os
import subprocess
import platform
import sys


def shell_command(program, args=None, no_errors=False):
    if args is None:
        args = []
    if isinstance(args, str):
        args = [args]

    if platform.system().lower() == "linux":
        args = [f'"{arg}"' for arg in args]
    args.insert(0, program)

    ret_code = subprocess.call(args, stderr=subprocess.STDOUT, shell=True)

    if ret_code and no_errors:
        raise Exception(f"Execute shell command error: ({program}): {ret_code}")
    return ret_code


def shell_command_ret(program, args=None):
    if args is None:
        args = []
    if isinstance(args, str):
        args = [args]

    if platform.system().lower() == "linux":
        args = [f'"{arg}"' for arg in args]
    args.insert(0, program)

    result_data = {"stdout": "", "stderr": ""}

    popen = subprocess.Popen(" ".join(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        result_data['stdout'] = stdout.strip().decode('utf-8', errors='ignore')
        result_data['stderr'] = stderr.strip().decode('utf-8', errors='ignore')
    finally:
        popen.stdout.close()
        popen.stderr.close()

    return result_data


def shell_command_in_dir(directory, program, args, no_errors=False):
    old_dir = os.getcwd()
    os.chdir(directory)
    ret = shell_command(program, args, no_errors)
    os.chdir(old_dir)
    return ret


def shell_command_ret_in_dir(directory, program, args, no_errors=False):
    old_dir = os.getcwd()
    os.chdir(directory)
    ret = shell_command_ret(program, args)
    os.chdir(old_dir)
    return ret
