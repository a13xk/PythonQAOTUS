#!/usr/bin/python3
import argparse
import subprocess


class FileSystemInfo:

    VERSION: str = "0.1"

    def __init__(self, cli_arguments: argparse.Namespace):
        self.version: bool = cli_arguments.version
        self.show_all_processes: bool = cli_arguments.show_all_processes

        self.res_all_processes: str = ""
    #

    def __del__(self):
        self.res_all_processes = ""
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

    def print_all_processes(self):
        """
        Print all running processes' information from console
        """
        self.res_all_processes = self.run_command_in_shell(command_args=[
            "ps", "aux"
        ])
        print("=== All processes ===")
        print(self.res_all_processes)
        print("=== END ===\n")
        exit()
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
    arg_parser.add_argument(
        "--show-all-processes",
        action="store_true",
        help="list all running processes"
    )
    args = arg_parser.parse_args()
    args.func(args)

    fs = FileSystemInfo(cli_arguments=args)
    if fs.version:
        fs.print_version()
    if fs.show_all_processes:
        fs.print_all_processes()
#
