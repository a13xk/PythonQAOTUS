#!/usr/bin/python3
import argparse
import subprocess


class FileSystemInfo:

    VERSION: str = "0.1"

    def __init__(self, cli_arguments: argparse.Namespace):
        self.version: bool = cli_arguments.version
    #

    def print_version(self):
        print(f"Version: {self.VERSION}")
        exit()
    #

    @staticmethod
    def run_command_in_shell(command_args: list) -> str:
        """
        Run Linux command in shell and return its output
        """
        command = " ".join([*command_args])
        shell_process = subprocess.run(
            args=command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding="utf-8",
            text=True
        )
        output = shell_process.stdout.rstrip()
        return output
    #
#


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog="file_system_info",
        description="Script interacting with Linux file system and process management"
    )
    arg_parser.set_defaults(func=lambda x: arg_parser.print_help())

    arg_parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="show version and exit"
    )
    args = arg_parser.parse_args()
    args.func(args)
#
