"""
=========================================================
Naphtech IDS Utilities
---------------------------------------------------------
Company   : Naphtech Hub
Developer : Naphtali Ishaya
Version   : 2.0.0
=========================================================
"""

import os
from datetime import datetime


APP_NAME = "Naphtech IDS"
COMPANY = "Naphtech Hub"
DEVELOPER = "Naphtali Ishaya"
VERSION = "2.0.0"
MOTTO = "Detect. Analyze. Defend."


def banner():
    """Display the application banner."""

    print("=" * 60)
    print(f"{COMPANY:^60}")
    print(f"{APP_NAME:^60}")
    print("-" * 60)
    print(f"Developer : {DEVELOPER}")
    print(f"Version   : {VERSION}")
    print(f"Motto     : {MOTTO}")
    print("=" * 60)


def clear_screen():
    """Clear the terminal screen."""

    os.system("clear")


def current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pause():
    """Pause until the user presses Enter."""

    input("\nPress Enter to continue...")


def divider():
    """Print a divider line."""

    print("-" * 60)
