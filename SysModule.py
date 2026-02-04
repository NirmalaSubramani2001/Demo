import re

def parse_logs(log_file):
    errors = []
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(r'ERROR|Exception|Timeout', line):
                errors.append(line.strip())
    return errors
