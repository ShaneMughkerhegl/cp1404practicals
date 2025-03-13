"""
Hex Colour Lookup
Estimate: 15 minutes
Actual:   17 minutes
"""

HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

def main():
    while True:
        colour_name = input("Enter a colour name: ").strip().title()
        if colour_name == "":
            break
        print(HEX_COLOURS.get(colour_name, "Invalid colour name"))

if __name__ == "__main__":
    main()