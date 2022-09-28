# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif 15 <= age <= 18:
#     print("drink coke")
# elif 18 <= age <= 21:
#     print("drink beer")
# elif age > 21:
#     print("drink whiskey")

age = int(input())
drink_type = ""
if age <= 14:
    drink_type = "drink toddy"
elif 15 <= age <= 18:
    drink_type = "drink coke"
elif 18 <= age <= 21:
    drink_type = "drink beer"
elif age > 21:
    drink_type = "drink whiskey"
print(f"{drink_type}")