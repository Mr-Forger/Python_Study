weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_c.items())


print(weather_f)