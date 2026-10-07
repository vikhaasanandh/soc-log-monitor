from detector.windows_log_collector import collect_windows_events
from detector.log_parser import parse_log_file
from detector.detection_engine import detect_threats
from detector.risk_analyzer import analyze_risk
from dashboard import generate_dashboard

def main():

    print("=" * 60)
    print("        SOC LOG MONITORING & THREAT DETECTION")
    print("=" * 60)

    print("\n[1/5] Collecting Windows Security events...")
    collect_windows_events()

    print("\n[2/5] Parsing security logs...")
    parse_log_file()

    print("\n[3/5] Detecting security threats...")
    detect_threats()

    print("\n[4/5] Analyzing security risk...")
    analyze_risk()

    print("\n[5/5] Generating SOC dashboard...")
    generate_dashboard()

    print("\n" + "=" * 60)
    print("              SOC ANALYSIS COMPLETED")
    print("=" * 60)

    print("\nReports generated:")
    print("  → reports/windows_events.json")
    print("  → reports/parsed_logs.json")
    print("  → reports/detections.json")
    print("  → reports/risk_summary.json")
    print("  → reports/soc_dashboard.html")


if __name__ == "__main__":
    main()