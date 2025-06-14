from datetime import datetime

class Grade:
    def __init__(self, id, student_id, subject, value, date=None, teacher_id=None, comment=None):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.value = value
        self.date = date if date else datetime.now().isoformat()
        self.teacher_id = teacher_id
        self.comment = comment

    def update_grade(self, value, comment=None):
        """Update the grade value and optionally add a comment."""
        self.value = value
        if comment is not None:
            self.comment = comment
        self.date = datetime.now().isoformat()

    def get_grade_info(self):
        """Return all grade info as a dict."""
        return {
            'id': self.id,
            'student_id': self.student_id,
            'subject': self.subject,
            'value': self.value,
            'date': self.date,
            'teacher_id': self.teacher_id,
            'comment': self.comment
        }