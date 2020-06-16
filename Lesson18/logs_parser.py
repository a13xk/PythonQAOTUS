import pathlib
import argparse
import re


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

    def get_total_number_of_requests(self) -> int:
        total = 0
        for log_file in self.log_files:
            with open(file=str(log_file), mode="r") as f:
                line_count = sum(1 for line in f if line != "")
            total += line_count
        return total
    #

    def get_requests_by_type(self) -> dict:
        all_requests = []
        pattern_request_type = re.compile(pattern=r'\]\s+"(GET|HEAD|POST|PUT|DELETE)\s+', flags=re.IGNORECASE)
        for log_file in self.log_files:
            with open(file=str(log_file), mode="r") as f:
                requests_by_type = {
                    "GET": 0,
                    "HEAD": 0,
                    "POST": 0,
                    "PUT": 0,
                    "DELETE": 0
                }
                for line in f.readlines():
                    match = pattern_request_type.search(string=line)
                    if match:
                        request_type = match.group(1)
                        if request_type == "GET":
                            requests_by_type["GET"] += 1
                        if request_type == "HEAD":
                            requests_by_type["HEAD"] += 1
                        if request_type == "POST":
                            requests_by_type["POST"] += 1
                        if request_type == "PUT":
                            requests_by_type["PUT"] += 1
                        if request_type == "DELETE":
                            requests_by_type["DELETE"] += 1
            all_requests.append(requests_by_type)
        all_requests_by_type = {
            "GET": 0,
            "HEAD": 0,
            "POST": 0,
            "PUT": 0,
            "DELETE": 0
        }
        for r in all_requests:
            all_requests_by_type["GET"] += r["GET"]
            all_requests_by_type["HEAD"] += r["HEAD"]
            all_requests_by_type["POST"] += r["POST"]
            all_requests_by_type["PUT"] += r["PUT"]
            all_requests_by_type["DELETE"] += r["DELETE"]
        return all_requests_by_type
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
