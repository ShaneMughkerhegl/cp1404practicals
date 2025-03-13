"""
Email to Name Dictionary
Estimate: 25 minutes
Actual:   28 minutes
"""

def extract_name(email):
    name_part = email.split('@')[0]
    return " ".join(name_part.split('.')).title()


def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm and confirm != 'y':
            name = input("Name: ").strip()
        email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()