import json
import re


INPUT_FILE = "reports/windows_events.json"
OUTPUT_FILE = "reports/detections.json"


def detect_threats():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        events = json.load(file)

    detections = []

    for event in events:

        event_id = event.get("Id")
        message = event.get("Message", "")
        source_ip = "Unknown"

        # Extract IPv4 address from Windows event message
        ip_match = re.search(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            message
        )

        if ip_match:
            source_ip = ip_match.group()

        # Failed login
        if event_id == 4625:

            detections.append({
                "threat_type": "Failed Login Attempt",
                "source_ip": source_ip,
                "severity": "HIGH",
                "event_id": event_id,
                "description": "Failed Windows login attempt detected."
            })

        # Special privileges
        elif event_id == 4672:

            detections.append({
                "threat_type": "Special Privilege Assignment",
                "source_ip": source_ip,
                "severity": "MEDIUM",
                "event_id": event_id,
                "description": "Special privileges were assigned to a new logon."
            })

        # Account created
        elif event_id == 4720:

            detections.append({
                "threat_type": "User Account Created",
                "source_ip": source_ip,
                "severity": "HIGH",
                "event_id": event_id,
                "description": "A new Windows user account was created."
            })

        # Security audit log cleared
        elif event_id == 1102:

            detections.append({
                "threat_type": "Security Log Cleared",
                "source_ip": source_ip,
                "severity": "CRITICAL",
                "event_id": event_id,
                "description": "Windows Security event log was cleared."
            })

        # User group enumeration
        elif event_id == 4798:

            detections.append({
                "threat_type": "User Group Enumeration",
                "source_ip": source_ip,
                "severity": "MEDIUM",
                "event_id": event_id,
                "description": "A user's local group membership was enumerated."
            })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(detections, file, indent=4)

    print(f"[+] Detected {len(detections)} security events.")
    print(f"[+] Results saved to: {OUTPUT_FILE}")

    return detections


if __name__ == "__main__":
    detect_threats()