def letter_to_gpa(letter: str) -> float:
    """Map a letter grade to its 4.33-scale GPA value."""
    letter = letter.strip().upper()     # tidy up input
    mapping = {
        "A+": 4.33, "A": 4.00, "A-": 3.67,
        "B+": 3.33, "B": 3.00, "B-": 2.67,
        "C+": 2.33, "C": 2.00, "C-": 1.67,
        "D+": 1.33, "D": 1.00, "D-": 0.67,
        "F": 0.00
    }
    if letter not in mapping:
        raise ValueError(f"Invalid grade '{letter}'")
    return mapping[letter]

def main() -> None:
    num_classes = int(input("How many classes have you taken? "))
    ap_classes  = int(input("How many of those were AP? "))

    gpa_total = 0.0
    for i in range(1, num_classes + 1):
        grade = input(f"Enter the letter grade for class {i} ")
        gpa_total += letter_to_gpa(grade)

    ap_bonus = ap_classes * 0.5            # 0.5 bump per AP
    overall_gpa = (gpa_total + ap_bonus) / num_classes
    print("Your GPA is:", round(overall_gpa, 3))

if __name__ == "__main__":
    main()
