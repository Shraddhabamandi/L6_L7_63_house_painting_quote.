import re


def _to_whole_number(text):
    """Helper: turns '120' into 120. Returns None if text is not a whole number."""
    if not isinstance(text, str):
        return None
    text = text.strip()
    # only plain digits 0-9 allowed (no minus sign, no letters, no decimals)
    if not re.fullmatch(r"[0-9]+", text):
        return None
    try:
        return int(text)
    except ValueError:  # e.g. extremely long digit strings
        return None


def clean_colour_name(name):
    """
    Turns a colour name into a lower-case code, e.g. 'Ocean Blue' -> 'ocean_blue'.
    Returns '' if name is not a string or is empty.
    """
    if not isinstance(name, str):
        return ""
    # split() handles spaces, tabs, new lines and extra spaces
    return "_".join(name.lower().split())


def room_area(text):
    """
    Converts 'LENGTHxWIDTH' into an area in square feet.
    Returns 0 if the input is not valid.
    """
    if not isinstance(text, str):
        return 0
    parts = text.lower().split("x")
    if len(parts) != 2:          # must be exactly one 'x'
        return 0
    length = _to_whole_number(parts[0])
    width = _to_whole_number(parts[1])
    if length is None or width is None:
        return 0
    return length * width


def total_wall_area(text):
    """
    Adds up wall areas separated by semicolons.
    Invalid or empty parts are skipped. Returns 0 if nothing is valid.
    """
    if not isinstance(text, str):
        return 0
    total = 0
    for part in text.split(";"):
        value = _to_whole_number(part)
        if value is not None:
            total += value
    return total


def main():
    print("==== Running clean_colour_name ====")
    value = input("Enter a paint colour name (e.g. Ocean Blue): ")
    print("Colour code:", clean_colour_name(value))

    print("\n==== Running room_area ====")
    value = input("Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): ")
    print("Room area (sq ft):", room_area(value))

    print("\n==== Running total_wall_area ====")
    value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
    print("Total wall area (sq ft):", total_wall_area(value))


if __name__ == "__main__":
    main()
