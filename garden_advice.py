"""
Garden Advice Application

Provides gardening advice based on month and season.
"""

month = input("Enter the current month: ").strip().lower()

if month in ["december", "january", "february"]:
    season = "Summer"
elif month in ["march", "april", "may"]:
    season = "Autumn"
elif month in ["june", "july", "august"]:
    season = "Winter"
elif month in ["september", "october", "november"]:
    season = "Spring"
else:
    season = "Unknown"

print(f"Season: {season}")

if season == "Summer":
    print("Water plants regularly and mulch to retain moisture.")
elif season == "Autumn":
    print("Prepare soil for winter and plant seasonal vegetables.")
elif season == "Winter":
    print("Protect sensitive plants from frost and reduce watering.")
elif season == "Spring":
    print("Plant flowers and vegetables and apply fertilizer.")
else:
    print("Invalid month entered.")

# TODO: Refactor the seasonal logic into reusable functions.
# TODO: Add proper documentation and docstrings.
# TODO: Replace hardcoded month lists with a dictionary or configuration file.
# TODO: Add error handling and input validation.
# TODO: Add support for gardeners in both Northern and Southern hemispheres.
