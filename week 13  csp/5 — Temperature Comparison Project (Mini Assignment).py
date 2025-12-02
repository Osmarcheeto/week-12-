# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
# Ask user for today's temperature
temperature = float(input("Enter today's temperature: "))

# Check if it's out of range
if temperature < -10 or temperature > 110:
    print("Extreme temperature warning!")
elif temperature < 50:
    print("It's cold.")
elif temperature < 85:
    print("It's warm.")
else:
    print("It's hot.")

