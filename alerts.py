
"""
Alert Center for Naphtech IDS

Developer : Naphtali Ishaya
Company   : Naphtech Hub
"""

import os

ALERT_LOG = "logs/alerts.log"


def view_alerts():
    """Display all recorded alerts."""

    print("\n========== ALERT HISTORY ==========\n")

    if not os.path.exists(ALERT_LOG):
        print("No alert log found.")
        return

    with open(ALERT_LOG, "r") as file:
        content = file.read().strip()

        if not content:
            print("No alerts recorded.")
        else:
            print(content)

    print("\n===================================\n")


def clear_alerts():
    """Clear the alert log."""

    with open(ALERT_LOG, "w") as file:
        file.write("")

    print("\n✅ Alert log cleared successfully.\n")

