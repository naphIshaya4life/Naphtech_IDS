

"""
Naphtech IDS
Main Application

Developer: Naphtali Ishaya
Company: Naphtech Hub
Version: 2.0.0
"""

from detector import DetectionEngine
from alerts import view_alerts, clear_alerts
engine = DetectionEngine()


def show_banner():
    print("=" * 55)
    print("              NAPHTECH HUB")
    print("             NAPHTECH IDS")
    print("                Version 2.0.0")
    print("-" * 55)
    print("Developer : Naphtali Ishaya")
    print("Status    : READY")
    print("=" * 55)


def show_menu():
    print("\nMAIN MENU")
    print("-" * 55)
    print("1. Start Monitoring")
    print("2. View Statistics")
    print("3. Alert Center")
    print("4. About")
    print("5. Exit")
    print("-" * 55)



def show_statistics():
    stats = engine.get_statistics()

    print("\n========== IDS STATISTICS ==========")
    print(f"Packets Processed : {stats['packets']}")
    print(f"Alerts Generated  : {stats['alerts']}")
    print(f"Threat Level      : {stats['threat']}")
    print(f"System Uptime     : {stats['uptime']}")
    print("====================================")


def about():
    print("\nNaphtech IDS")
    print("Developer : Naphtali Ishaya")
    print("Company   : Naphtech Hub")
    print("Language  : Python")
    print("Version   : 2.0.0")

def alert_center():
    """
    Display the Alert Center menu.
    """

    while True:

        print("\n========== ALERT CENTER ==========")
        print("1. View Alerts")
        print("2. Clear Alerts")
        print("3. Back")
        print("==================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            view_alerts()

        elif choice == "2":
            clear_alerts()

        elif choice == "3":
            break

        else:
            print("\nInvalid option. Please try again.")



def main():

    show_banner()

    while True:

        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            engine.monitor_network()

        elif choice == "2":
            show_statistics()


        elif choice == "3":
            alert_center()

        elif choice == "4":
            about()

        elif choice == "5":
            print("\nThank you for using Naphtech IDS.")
            break

        else:
            print("\nInvalid option. Try again.")


if __name__ == "__main__":
    main()
