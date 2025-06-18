def convert_to_gpa(percentage):
    if 98 <= percentage <= 100:
        return 4.33
    elif 93 <= percentage < 98:
        return 4.0
    elif 90 <= percentage < 93:
        return 3.67
    elif 87 <= percentage < 90:
        return 3.33
    elif 83 <= percentage < 87:
        return 3.0
    elif 80 <= percentage < 83:
        return 2.67
    elif 77 <= percentage < 80:
        return 2.33
    elif 73 <= percentage < 77:
        return 2.0
    elif 70 <= percentage < 73:
        return 1.67
    elif 67 <= percentage < 70:
        return 1.33
    elif 63 <= percentage < 67:
        return 1.0
    elif 60 <= percentage < 63:
        return 0.67
    else:
        return 0.0

num_classes = int(input("How many classes have you took "))
gpa_total = 0

ap_classes = int(input("How many AP classes have you took "))
ap_bonus = ap_classes * 0.5

for i in range(1, num_classes + 1):
    percent = int(input(f"Enter your percentage for class {i}: "))
    gpa = convert_to_gpa(percent)
    gpa_total += gpa

total_gpa = (gpa_total + ap_bonus) / num_classes
print("Your GPA is -", round(total_gpa, 3))

