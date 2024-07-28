"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.00
# Number of characters.
numChars = 18
# Color of characters.
Color = "black"
# Type of wood.
Wood = "oak"

# Write assignment and if statements here as appropriate.
if numChars > 5:
  charge = charge + (numChars - 5) * 4
if Wood == "oak":
    charge = charge + 20
if Color == "gold":
  charge = charge + 15
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
print("2024/07/28_LeeAnthony_4-1")
