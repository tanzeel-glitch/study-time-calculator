def main():
    try:
        hours_per_day = float(input("Hours available per day: "))
        subjects = int(input("Number of subjects: "))
        exam_days_left = int(input("Exam days left: "))

        if hours_per_day <= 0 or subjects <= 0 or exam_days_left <= 0:
            print("Please enter positive numbers.")
            return

        daily_hours_per_subject = hours_per_day / subjects
        total_hours_per_subject = daily_hours_per_subject * exam_days_left

        print("\nSuggested study plan")
        print(f"Study {daily_hours_per_subject:.2f} hours per subject each day.")
        print(
            f"That gives you about {total_hours_per_subject:.2f} "
            f"hours per subject over {exam_days_left} days."
        )

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
