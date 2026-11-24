MIN_SCORE = 0
MAX_SCORE = 100

GRADE_A_MIN = 90
GRADE_B_MIN = 80
GRADE_C_MIN = 70
GRADE_D_MIN = 60


def letter_grade(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")

    if score >= GRADE_A_MIN:
        return "A"
    if score >= GRADE_B_MIN:
        return "B"
    if score >= GRADE_C_MIN:
        return "C"
    if score >= GRADE_D_MIN:
        return "D"
    return "F"
