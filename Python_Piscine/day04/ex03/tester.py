from new_student import Student


def main():
    """main tester"""
    student = Student(name="Edward", surname="agle")
    print(student)


def main_error():
    """main tester with error"""
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    try:
        main()
        main_error()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
