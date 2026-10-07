"""
Garden Advice Application

Provides gardening advice based on month, hemisphere, and season.
"""

MONTH_TO_SEASON = {
    "northern": {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Autumn", 10: "Autumn", 11: "Autumn"
    },
    "southern": {
        12: "Summer", 1: "Summer", 2: "Summer",
        3: "Autumn", 4: "Autumn", 5: "Autumn",
        6: "Winter", 7: "Winter", 8: "Winter",
        9: "Spring", 10: "Spring", 11: "Spring"
    }
}


def get_season(month, hemisphere):
    """Determine season based on month and hemisphere."""
    return MONTH_TO_SEASON.get(
        hemisphere.lower(), {}
    ).get(month, "Unknown")


def get_advice(season):
    """Return gardening advice for a season."""
    advice = {
        "Summer": "Water plants regularly and mulch to retain moisture.",
        "Autumn": "Prepare soil for winter and plant seasonal vegetables.",
        "Winter": "Protect sensitive plants from frost and reduce watering.",
        "Spring": "Plant flowers and vegetables and apply fertilizer."
    }

    return advice.get(season, "Invalid season entered.")


def validate_month(month):
    """Validate month input."""
    return 1 <= month <= 12


def main():
    """Main application entry point."""

    try:
        month = int(input("Enter month number (1-12): "))
        hemisphere = input(
            "Enter hemisphere (Northern/Southern): "
        ).strip().lower()

        if not validate_month(month):
            print("Error: Month must be between 1 and 12.")
            return

        if hemisphere not in ["northern", "southern"]:
            print("Error: Hemisphere must be Northern or Southern.")
            return

        season = get_season(month, hemisphere)

        print(f"Season: {season}")
        print(get_advice(season))

    except ValueError:
        print("Error: Please enter a valid number for the month.")


if __name__ == "__main__":
    main()
