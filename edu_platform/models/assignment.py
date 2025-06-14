class Assignment:
    def __init__(self, id, title, description, deadline, subject, teacher_id, class_id):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.submissions = {}
        self.grades = {}

    def add_submission(self, student_id, content):
        self.submissions[student_id] = content
        return f"Submission added for student {student_id}."

    def set_grade(self, student_id, grade):
        self.grades[student_id] = grade
        return f"Grade set for student {student_id}."

    def get_status(self, student_id):
        return self.submissions.get(student_id, 'not found')