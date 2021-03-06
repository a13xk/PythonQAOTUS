#!/usr/bin/python3
import argparse
import os
import subprocess
import sys


class FileSystemInfo:

    VERSION: str = "0.1"

    def __init__(self, cli_arguments: argparse.Namespace):
        self.version: bool = cli_arguments.version
        self.show_all_processes: bool = cli_arguments.show_all_processes
        self.process_id: int = cli_arguments.process_id
        self.directory: str = cli_arguments.list_files
        self.show_kernel_release: bool = cli_arguments.show_kernel_release
        self.show_os_version: bool = cli_arguments.show_os_version

        self.res_all_processes: str = ""
        self.res_process: str = ""
        self.res_kernel_release: str = ""
        self.res_os_version: str = ""
    #

    def __del__(self):
        self.res_all_processes = ""
        self.res_process = ""
        self.res_kernel_release = ""
        self.res_os_version = ""
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

    def print_process_info(self):
        """
        Print information on specified process by its id
        """
        print(f"=== Information on process #{self.process_id} ===")
        self.res_process = self.run_command_in_shell(command_args=[
            "ps", "aux", "|",
            "grep", str(self.process_id), "|",
            "grep", "-v", "grep", "|",
            "grep", "-v", f"{__file__}"
        ])
        print(self.res_process)
        print("=== END ===\n")
        exit()
    #

    def print_files_in_directory(self):
        """
        Print all files in given directory
        """
        if not self.directory or self.directory == ".":
            self.directory = os.path.abspath(os.getcwd())
        if "~" in self.directory:
            self.directory = os.path.expanduser(self.directory)
        if not os.path.isdir(self.directory):
            print(f"Directory specified by path '{self.directory}' does not exist")
            exit()
        else:
            all_files = [os.path.join(self.directory, file) for file in os.listdir(path=self.directory)
                         if os.path.isfile(os.path.join(self.directory, file))]
            all_files = sorted(all_files, key=str.casefold)

            print("=== Files in directory ===")
            print(f"Directory:\n\t{self.directory}")
            print("Files:")
            for f in all_files:
                print(f"\t{f}")
            print("=== END ===\n")
            exit()
    #

    def print_kernel_release(self):
        """
        Print Linux kernel version
        """
        self.res_kernel_release = self.run_command_in_shell(command_args=[
            "uname", "-r"
        ])
        print("=== Linux kernel version ===")
        print(self.res_kernel_release)
        print("=== END ===\n")
        exit()
    #

    def print_os_version(self):
        """
        Print Linux OS version
        """
        self.res_os_version = self.run_command_in_shell(command_args=[
            "lsb_release", "-d", "|",
            "awk", "'{$1=\"\"; print $0}'", "|",
            "awk", "'{$1=$1};1'"
        ])
        print("=== Linux OS version ===")
        print(self.res_os_version)
        print("=== END ===\n")
        exit()
    #
#


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=27),
        prog="file_system_info",
        description="Script interacting with Linux file system and process management"
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="show version and exit"
    )
    parser.add_argument(
        "--show-all-processes",
        action="store_true",
        help="list all running processes"
    )
    parser.add_argument(
        "--process-id",
        metavar="PID",
        action="store",
        type=int,
        help="show information on particular process with specified PID"
    )
    parser.add_argument(
        "--list-files",
        metavar="DIR",
        nargs="?",
        const=".",
        action="store",
        type=str,
        help="list files in given directory (current directory by default)"
    )
    parser.add_argument(
        "--show-kernel-release",
        action="store_true",
        help="show Linux kernel version"
    )
    parser.add_argument(
        "--show-os-version",
        action="store_true",
        help="show Linux OS version"
    )

    args = parser.parse_args()

    # Optional: display builtin help without -h|--help CLI options as well
    if len(sys.argv) == 1:
        parser.print_help()
        exit()

    fs = FileSystemInfo(cli_arguments=args)
    if fs.version:
        fs.print_version()
    if fs.show_all_processes:
        fs.print_all_processes()
    if fs.process_id:
        fs.print_process_info()
    if fs.directory:
        fs.print_files_in_directory()
    if fs.show_kernel_release:
        fs.print_kernel_release()
    if fs.show_os_version:
        fs.print_os_version()
#
