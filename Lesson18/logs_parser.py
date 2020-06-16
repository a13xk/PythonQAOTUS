import pathlib
import argparse


class LogsParser:

    def __init__(self, logs_source: str, json_file: str):
        self.logs_source: pathlib.Path = pathlib.Path(logs_source)
        self.json_file: pathlib.Path = pathlib.Path(json_file)

        self.log_files = []

        if self.logs_source.is_dir():
            self.log_files = sorted(list([log_file.absolute() for log_file in sorted(pathlib.Path(self.logs_source).glob("**/*"))]))
        elif self.logs_source.is_file():
            self.log_files.append(self.logs_source.absolute())
        else:
            raise FileExistsError("Incorrect path to source folder or log file")
    #
#


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog="log_parser",
        description="NGINX logs parser example. Collects the following statistics:\n"
                    "- Total number of requests\n"
                    "- Number of requests by type: GET - 20, POST - 10, etc.\n"
                    "- Top 10 IP addresses used to make requests\n"
                    "- Top 10 longest requests (include method, URL, IP address, time)\n"
                    "- Top 10 requests resulted with client error 4xx (include method, URL, status code, IP address)\n"
                    "- Top 10 requests resulted with server error 5xx (include method, URL, status code, IP address)"
    )
    arg_parser.add_argument(
        "-i",
        "--input",
        action="store",
        help="Path to directory with log files or path to specific log file"
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        action="store",
        help="Path to output JSON file where to save collected statistics"
    )
    args = arg_parser.parse_args()
#
