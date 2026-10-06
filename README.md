## 📊 SOC Dashboard

![SOC Threat Detection Dashboard](https://raw.githubusercontent.com/vikhaasanandh/soc-log-monitor/main/screenshots/soc_dashboard.png)

The project generates an interactive HTML dashboard showing:

- Total security events
- Critical, High, Medium, and Low severity events
- Threat distribution
- Source IP activity
- Detected security events
- Overall security risk

## 🛠️ Technologies Used

- Python
- Windows Security Event Logs
- PowerShell
- JSON
- HTML5
- CSS3
- JavaScript
- Git & GitHub

## 📂 Project Structure

```text
soc-log-monitor/
├── detector/
│   ├── detection_engine.py
│   ├── log_parser.py
│   ├── risk_analyzer.py
│   └── windows_log_collector.py
├── sample_logs/
│   └── auth.log
├── screenshots/
├── reports/
├── dashboard.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md