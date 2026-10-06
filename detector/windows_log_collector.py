import json
import subprocess

OUTPUT_FILE = "reports/windows_events.json"


def collect_windows_events(max_events=100):

    print("[*] Collecting Windows Security events...")

    command = [
        "powershell",
        "-Command",
        f"Get-WinEvent -LogName Security -MaxEvents {max_events} | "
        "Select-Object TimeCreated, Id, LevelDisplayName, ProviderName, Message | "
        "ConvertTo-Json -Depth 3"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        if not result.stdout.strip():
            print("[!] No Windows Security events found.")
            return []

        events = json.loads(result.stdout)

        if isinstance(events, dict):
            events = [events]

        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                events,
                file,
                indent=4,
                default=str
            )

        print(f"[+] Collected {len(events)} Windows Security events.")
        print(f"[+] Results saved to: {OUTPUT_FILE}")

        return events

    except subprocess.CalledProcessError as error:

        print("[!] Unable to access Windows Security logs.")
        print(error)

        return []

    except json.JSONDecodeError:

        print("[!] Unable to parse Windows event data.")

        return []


if __name__ == "__main__":
    collect_windows_events()