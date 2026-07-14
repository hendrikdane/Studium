def calculate_grade(score, max_score=100):
    percentage=(score/max_score)*100
    if percentage>=90:
        print("A")
    elif percentage>=80:
        print("B")
    elif percentage>=70:
        print("C")
    else:
        print("F")
        