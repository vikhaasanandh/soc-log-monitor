import re
import json


LOG_FILE = "sample_logs/auth.log"
OUTPUT_FILE = "reports/parsed_logs.json"


def parse_log_line(line):
    """Extract security information from one SSH log line."""

    result = {
        "raw_log": line.strip(),
        "timestamp": None,
        "username": None,
        "source_ip": None,
        "source_port": None,
        "event_type": "unknown",
        "invalid_user": False
    }

    # Extract timestamp
    timestamp_match = re.search(
        r"^([A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2})",
        line
    )

    if timestamp_match:
        result["timestamp"] = timestamp_match.group(1)

    # Extract source IP
    ip_match = re.search(
        r"from\s+(\d{1,3}(?:\.\d{1,3}){3})",
        line
    )

    if ip_match:
        result["source_ip"] = ip_match.group(1)

    # Extract source port
    port_match = re.search(
        r"port\s+(\d+)",
        line
    )

    if port_match:
        result["source_port"] = int(port_match.group(1))

    # Detect invalid user
    invalid_match = re.search(
        r"Failed password for invalid user\s+(\S+)",
        line
    )

    if invalid_match:
        result["username"] = invalid_match.group(1)
        result["event_type"] = "failed_login"
        result["invalid_user"] = True
        return result

    # Detect failed login
    failed_match = re.search(
        r"Failed password for\s+(\S+)",
        line
    )

    if failed_match:
        result["username"] = failed_match.group(1)
        result["event_type"] = "failed_login"
        return result

    # Detect successful login
    success_match = re.search(
        r"Accepted password for\s+(\S+)",
        line
    )

    if success_match:
        result["username"] = success_match.group(1)
        result["event_type"] = "successful_login"
        return result

    return result


def parse_log_file():

    parsed_logs = []

    with open(LOG_FILE, "r") as file:

        for line in file:

            if line.strip():

                parsed_event = parse_log_line(line)

                parsed_logs.append(parsed_event)

    with open(OUTPUT_FILE, "w") as file:

        json.dump(
            parsed_logs,
            file,
            indent=4
        )

    print(f"[+] Parsed {len(parsed_logs)} log events.")
    print(f"[+] Results saved to: {OUTPUT_FILE}")

    return parsed_logs


if __name__ == "__main__":
    parse_log_file()    