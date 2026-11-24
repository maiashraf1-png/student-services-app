from dataclasses import dataclass
from enum import Enum


class StudentType(Enum):
    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass
class Course:
    hours: int


RATE_PER_HOUR = {
    StudentType.REGULAR: 350,
    StudentType.STAFF_CHILD: 175,
    StudentType.SCHOLARSHIP: 0,
}

HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


def tuition_fee(courses, student_type, summer=False, discount=0, extras=()):
    total = sum(course.hours * RATE_PER_HOUR[student_type] for course in courses)

    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE

    total -= discount
    total += sum(extras)
    return total


def fee_report(courses, student_type, summer=False, discount=0):
    fee = tuition_fee(courses, student_type, summer, discount)
    lines = []

    if student_type == StudentType.REGULAR:
        lines.append(f"Student fee: {fee}")
    elif student_type == StudentType.STAFF_CHILD:
        lines.append(f"Staff child fee: {fee}")

    if fee > HIGH_FEE_THRESHOLD:
        lines.append("High fee")

    return "\n".join(lines)


def process_all(students):
    fees = {}
    for student in students:
        fees[student["name"]] = tuition_fee(
            student["courses"],
            student["type"],
            student["summer"],
        )
    return fees
