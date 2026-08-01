"""
Naphtech IDS
Main Application
"""

from utils import banner
from dashboard import display_menu, get_user_choice


def start_monitoring():
    print("\n[INFO] Monitoring engine coming in Mission 007...\n")


def show_dashboard():
    print("\n[INFO] Live dashboard coming soon...\n")


def main():
    banner()

    while True:
        display_menu()

        choice = get_user_choice()

        if choice == "1":
            start_monitoring()

        elif choice == "2":
            show_dashboard()

        elif choice == "3":
            print("\nAlert history coming soon.\n")

        elif choice == "4":
            print("\nAttack statistics coming soon.\n")

        elif choice == "5":
            print("\nReport generation coming soon.\n")

        elif choice == "6":
            print("\nSettings coming soon.\n")

        elif choice == "7":
            print("\nNaphtech IDS")
            print("Developer: Naphtali Ishaya")
            print("Company: Naphtech Hub\n")

        elif choice == "8":
            print("\nThank you for using Naphtech IDS.")
            break

        else:
            print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    main()
