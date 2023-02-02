from scripts import shell
from scripts import git
from scripts import move
from scripts import notify

import os
import argparse
import multiprocessing

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
BUILD_FOLDER = os.path.join(ROOT_FOLDER, "build")
BIN_FOLDER = os.path.join(ROOT_FOLDER, "dist")

# Arguments
arg_parser = argparse.ArgumentParser(prog='Build script')
arg_parser.add_argument("--debug", dest="debug", help="Build with debug", action="store_true", default=False)
arg_parser.add_argument("--package", dest="package", help="Выполнять сборку в пакеты", action="store_true", default=False)
args = arg_parser.parse_args()


def run_configure():
    if not os.path.exists(BUILD_FOLDER):
        os.mkdir(BUILD_FOLDER)

    cmake_args = [
        "'-G Unix Makefiles'", "..",
        "-DCMAKE_BUILD_TYPE=" + ("Debug" if args.debug else "Release")
    ]
    print(BUILD_FOLDER)
    shell.command_in_dir(BUILD_FOLDER, "cmake", cmake_args)


def run_build():
    cmake_args = [
        "--build", ".",
        "--config", "Debug" if args.debug else "Release",
        "--", "-j", str(multiprocessing.cpu_count())
    ]

    shell.command_in_dir(BUILD_FOLDER, "cmake", cmake_args)


def main():
    run_configure()
    run_build()

    if args.package:
        mv = move.Move(BUILD_FOLDER, BIN_FOLDER)
        mv.copy()

    notify.info('Build App', 'Building application finished!')


if __name__ == "__main__":
    main()
