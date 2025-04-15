
SQUARE_FEET_PER_ACRE = 43560


length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

area_sq_ft = length * width

area_acres = area_sq_ft / SQUARE_FEET_PER_ACRE


print(f"The area of the field is {area_acres:.2f} acres.")
