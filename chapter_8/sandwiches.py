def sandwiches(*items):
    """Displays a list of items a person wants on a sandwich."""
    print("\nThe following items were selected for a sandwich:")
    for item in items:
        print("- " + item.upper())

sandwiches('mustard', 'chicken cullet', 'sharp chedder')
