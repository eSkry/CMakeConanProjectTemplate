import os

from scripts import shell
import platform


_IS_WINDOWS = platform.system().lower() == "windows"


def info(title, message):
    if _IS_WINDOWS:
        shell.command_in_dir("scripts/misc", "notify.bat", [title, message])
    else:
        shell.command("notify-send", ["-i", "info", title, message])


def error(title, message):
    if _IS_WINDOWS:
        shell.command_in_dir("scripts/misc", "notify.bat", [title, message])
    else:
        shell.command("notify-send", ["-i", "error", title, message])


def warning(title, message):
    if _IS_WINDOWS:
        shell.command_in_dir("scripts/misc", "notify.bat", [title, message])
    else:
        shell.command("notify-send", ["-i", "important", title, message])
