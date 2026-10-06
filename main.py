from detector.log_parser import parse_log_file
from detector.detection_engine import detect_threats
from detector.risk_analyzer import analyze_risk
from dashboard import generate_dashboard


def main():

    print("=" * 60)
    print("        SOC LOG MONITORING & THREAT DETECTION")
    print("=" * 60)

    print("\n[1/4] Parsing security logs...")
    parse_log_file()

    print("\n[2/4] Detecting security threats...")
    detect_threats()

    print("\n[3/4] Analyzing security risk...")
    analyze_risk()

    print("\n[4/4] Generating SOC dashboard...")
    generate_dashboard()

    print("\n" + "=" * 60)
    print("              SOC ANALYSIS COMPLETED")
    print("=" * 60)

    print("\nReports generated:")
    print("  → reports/parsed_logs.json")
    print("  → reports/detections.json")
    print("  → reports/risk_summary.json")
    print("  → reports/soc_dashboard.html")


if __name__ == "__main__":
    main()