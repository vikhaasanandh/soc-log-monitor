import json


INPUT_FILE = "reports/detections.json"
OUTPUT_FILE = "reports/risk_summary.json"


SEVERITY_LEVELS = {
    "CRITICAL": 4,
    "HIGH": 3,
    "MEDIUM": 2,
    "LOW": 1
}


def analyze_risk():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        detections = json.load(file)

    critical = 0
    high = 0
    medium = 0
    low = 0

    for detection in detections:

        event_id = detection.get("event_id")

        # Refine severity based on Windows Event ID
        if event_id == 1102:
            detection["severity"] = "CRITICAL"

        elif event_id == 4625:
            detection["severity"] = "HIGH"

        elif event_id == 4720:
            detection["severity"] = "HIGH"

        elif event_id == 4672:
            detection["severity"] = "MEDIUM"

        elif event_id == 4798:
            detection["severity"] = "LOW"

        severity = detection.get(
            "severity",
            "LOW"
        ).upper()

        if severity == "CRITICAL":
            critical += 1

        elif severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        else:
            low += 1

    # Determine overall risk
    if critical > 0:
        overall_risk = "CRITICAL"

    elif high > 0:
        overall_risk = "HIGH"

    elif medium > 0:
        overall_risk = "MEDIUM"

    else:
        overall_risk = "LOW"

    summary = {
        "total_security_events": len(detections),
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low,
        "overall_risk": overall_risk
    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )

    print("\n[+] Risk analysis completed.")
    print(f"[+] Total security events: {len(detections)}")
    print(f"[+] Critical: {critical}")
    print(f"[+] High: {high}")
    print(f"[+] Medium: {medium}")
    print(f"[+] Low: {low}")
    print(f"[+] Overall risk: {overall_risk}")
    print(f"[+] Results saved to: {OUTPUT_FILE}")

    return summary


if __name__ == "__main__":
    analyze_risk()