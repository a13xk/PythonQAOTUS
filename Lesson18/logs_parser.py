import argparse
import json
import pathlib
import re
from collections import Counter
from typing import List


class LogsParser:

    def __init__(self, logs_source: str, json_file: str):
        self.logs_source: pathlib.Path = pathlib.Path(logs_source)
        self.json_file: pathlib.Path = pathlib.Path(json_file).absolute()

        self.log_files = []

        if self.logs_source.is_dir():
            self.log_files = sorted(list([log_file.absolute() for log_file in sorted(self.logs_source.glob("**/*"))]))
        elif self.logs_source.is_file():
            self.log_files.append(self.logs_source.absolute())
        else:
            raise FileExistsError("Incorrect path to source folder or log file")
        # Group 1: IPv4/6
        # Group 2: HTTP method
        # Group 3: URL
        # Group 4: response code
        # Group 5: request duration
        self.LOG_LINE_PATTERN = re.compile(
            pattern=r'((?:\d{1,3}\.){3}\d{1,3}|(?:[a-f0-9]{1,4}:){7}[a-f0-9]{1,4})\s+-\s+-\s+\[.*?\+\d+\]\s+"(GET|HEAD|POST|PUT|DELETE)\s+(\/.*?)\s+HTTP\/1\.1"\s+(\d+)\s+(\d+)',
            flags=re.IGNORECASE
        )
    #

    def save_report(self):
        with open(file=str(self.json_file), mode="w") as f:
            data = {
                "requests_total": self.get_total_number_of_requests(),
                "requests_by_type": self.get_requests_by_type(),
                "top_10_ip_addresses": self.get_top_10_ip_addresses(),
                "top_10_longest_requests": self.get_top_10_longest_requests()
            }
            f.write(json.dumps(data, indent=4))
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
                    match = self.LOG_LINE_PATTERN.search(string=line)
                    if match:
                        request_type = match.group(2)
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

    def get_top_10_ip_addresses(self) -> List[dict]:
        ip_addresses = []
        for log_file in self.log_files:
            with open(file=str(log_file), mode="r") as f:
                for line in f.readlines():
                    match = self.LOG_LINE_PATTERN.search(string=line)
                    if match:
                        ip_addresses.append(match.group(1))
        top_10_addresses = []
        for ip in Counter(ip_addresses).most_common(n=10):
            top_10_addresses.append({"ip": ip[0], "count": ip[1]})
        return top_10_addresses
    #

    def get_top_10_longest_requests(self) -> List[dict]:
        all_requests = []
        for log_file in self.log_files:
            with open(file=str(log_file), mode="r") as f:
                for line in f.readlines():
                    match = self.LOG_LINE_PATTERN.search(string=line)
                    if match:
                        all_requests.append(
                            {
                                "method": match.group(2),
                                "url": match.group(3),
                                "ip": match.group(1),
                                "duration": int(match.group(5))
                            }
                        )
        top_10_longest = sorted(all_requests, key=lambda d: d["duration"], reverse=True)[0:10]
        return top_10_longest
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
        "--input",
        action="store",
        help="Path to directory with log files or path to specific log file"
    )
    arg_parser.add_argument(
        "--output",
        action="store",
        help="Path to output JSON file where to save collected statistics"
    )
    args = arg_parser.parse_args()

    logs_parser = LogsParser(logs_source=args.input, json_file=args.output)
    logs_parser.save_report()
#
