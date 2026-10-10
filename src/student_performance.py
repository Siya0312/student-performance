"""Student CGPA Performance Management System."""

from collections.abc import Sequence
from typing import TypedDict


class PerformanceSummary(TypedDict):
    """Structured output for a student's CGPA and performance summary."""

    cgpa: float
    performance: str


def _validate_course_data(
    grade_points: Sequence[float],
    credits: Sequence[float],
) -> None:
    """Validate course grade points and credits before calculation."""
    if not grade_points or not credits:
        raise ValueError("Grade points and credits cannot be empty.")

    if len(grade_points) != len(credits):
        raise ValueError("Grade points and credits must have the same length.")

    if any(not 0 <= point <= 10 for point in grade_points):
        raise ValueError("Grade points must be between 0 and 10.")

    if any(credit <= 0 for credit in credits):
        raise ValueError("Credits must be greater than zero.")


def calculate_cgpa(
    grade_points: list[float],
    credits: list[float],
) -> float:
    """Calculate CGPA using credit-weighted grade points."""
    _validate_course_data(grade_points, credits)

    total_credits = sum(credits)
    weighted_points = sum(
        point * credit for point, credit in zip(grade_points, credits, strict=True)
    )

    return round(weighted_points / total_credits, 2)


def summarize_performance(
    grade_points: Sequence[float],
    credits: Sequence[float],
) -> PerformanceSummary:
    """Return a structured summary of CGPA and performance category."""
    cgpa = calculate_cgpa(list(grade_points), list(credits))

    return {
        "cgpa": cgpa,
        "performance": get_performance(cgpa),
    }


def get_performance(cgpa: float) -> str:
    """Return a performance category based on CGPA."""
    if not 0 <= cgpa <= 10:
        raise ValueError("CGPA must be between 0 and 10.")

    thresholds = (
        (9, "Outstanding"),
        (8, "Excellent"),
        (7, "Good"),
        (6, "Satisfactory"),
    )

    for minimum, label in thresholds:
        if cgpa >= minimum:
            return label

    return "Needs Improvement"


def main() -> None:
    """Run a demonstration of the CGPA management system."""
    grade_points = [9.0, 8.5, 8.0, 9.5]
    credits = [4, 3, 3, 2]

    summary = summarize_performance(grade_points, credits)

    print("Student CGPA Performance Management System")
    print("-" * 42)
    print(f"Calculated CGPA: {summary['cgpa']:.2f}")
    print(f"Performance: {summary['performance']}")


if __name__ == "__main__":
    main()
