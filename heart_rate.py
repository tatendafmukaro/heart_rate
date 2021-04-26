"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
# Check Point 1 by Felix

user_age = int(input(" Please enter your age: "))
maximum_range = 220 -  user_age
lower_percentage = maximum_range * 0.65
higher_percentage = maximum_range * 0.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_percentage: .0f} and {higher_percentage: .0f} beats per minute.")