MIN_SCORE = 0
MAX_SCORE = 100

GRADE_THRESHOLDS = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
)


def letter_grade(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")

    for minimum, grade in GRADE_THRESHOLDS:
        if score >= minimum:
            return grade
    return "F"