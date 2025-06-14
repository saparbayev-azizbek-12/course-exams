import os
import pandas as pd
from .user import User, Role

class Student(User):
    def __init__(self, id, full_name, email, password, role: Role, grade, subjects=None):
        super().__init__(id, full_name, email, password, role)
        self.student_id = id
        self.grade = grade
        self.subjects = subjects if subjects is not None else {}
        self.assignments = {}
        self.grades = {}

    def view_assignments(self):
        if not os.path.exists('data/assignments.csv'):
            return False
        
        df = pd.read_csv('data/assignments.csv').to_string(index=False)
        return df

    def submit_assignment(self, assignment_id, content):
        path = 'data/student_assignments.csv'
        if not os.path.exists(path):
            df = pd.DataFrame(columns=['Student ID', 'Assignment ID', 'Content'])
        else:
            df = pd.read_csv(path)
        new_entry = {'Student ID': self.student_id, 'Assignment ID': assignment_id, 'Content': content}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(path, index=False)
        return "Topshiriq jo'natildi"

    def view_grades(self):
        path = 'data/student_assignments.csv'
        if os.path.exists(path):
            df = pd.read_csv(path)
            return df[['Assignment ID', 'Grade']].to_string(index=False)
        return 'Baholar mavjud emas'

    def calculate_average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            all_grades.extend(grade_list)
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)
    