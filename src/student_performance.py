"""Student CGPA Performance Management System."""


def calculate_cgpa(grade_points: list[float], credits: list[float]) -> float:
    """Calculate CGPA using credit-weighted grade points."""
    if not grade_points or not credits:
        raise ValueError("Grade points and credits cannot be empty.")

    if len(grade_points) != len(credits):
        raise ValueError("Grade points and credits must have equal lengths.")

    if any(point < 0 or point > 10 for point in grade_points):
        raise ValueError("Grade points must be between 0 and 10.")

    if any(credit <= 0 for credit in credits):
        raise ValueError("Credits must be greater than zero.")

    total_credits = sum(credits)
    weighted_points = sum(
        point * credit for point, credit in zip(grade_points, credits, strict=True)
    )

    return round(weighted_points / total_credits, 2)


def get_performance(cgpa: float) -> str:
    """Return a performance category based on CGPA."""
    if not 0 <= cgpa <= 10:
        raise ValueError("CGPA must be between 0 and 10.")

    if cgpa >= 9:
        return "Outstanding"
    if cgpa >= 8:
        return "Excellent"
    if cgpa >= 7:
        return "Good"
    if cgpa >= 6:
        return "Satisfactory"
    return "Needs Improvement"


def main() -> None:
    """Run a demonstration of the CGPA management system."""
    grade_points = [9.0, 8.5, 8.0, 9.5]
    credits = [4, 3, 3, 2]

    cgpa = calculate_cgpa(grade_points, credits)
    performance = get_performance(cgpa)

    print("Student CGPA Performance Management System")
    print("-" * 42)
    print(f"Calculated CGPA: {cgpa:.2f}")
    print(f"Performance: {performance}")


if __name__ == "__main__":
    main()
