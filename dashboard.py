
"""
==========================================================
Naphtech IDS Dashboard

Developer : Naphtali Ishaya
Company   : Naphtech Hub
Version   : 2.0.0

Description:
Professional terminal dashboard for monitoring
the Naphtech Intrusion Detection System.
==========================================================
"""


def show_dashboard(stats):
    """
    Display the professional IDS dashboard.
    """

    print("\n")
    print("=" * 60)
    print("                 NAPHTECH HUB")
    print("          Intrusion Detection System")
    print("                 Version 2.0.0")
    print("=" * 60)

    print(f"🛡  System Status : ACTIVE")
    print(f"🚦 Threat Level  : {stats['threat']}")
    print(f"📈 Threat Meter  : {stats['meter']}")

    print("-" * 60)

    print(f"📦 Packets Seen  : {stats['packets']}")
    print(f"🚨 Alerts Raised : {stats['alerts']}")
    print(f"🌍 Unique IPs    : {stats.get('unique_ips', 'N/A')}")
    print(f"⏱  Uptime       : {stats['uptime']}")

    print("-" * 60)

    print("Developer : Naphtali Ishaya")
    print("Company   : Naphtech Hub")
    print("Status    : Monitoring Network Traffic")

    print("=" * 60)

