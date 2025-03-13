"""
State Names Lookup
Estimate: 15 minutes
Actual:   18 minutes
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

def main():
    while True:
        state_code = input("Enter short state: ").strip().upper()
        if state_code == "":
            break
        try:
            print(f"{state_code} is {STATE_NAMES[state_code]}")
        except KeyError:
            print("Invalid state code")

    for key, value in STATE_NAMES.items():
        print(f"{key:3} is {value}")

if __name__ == "__main__":
    main()