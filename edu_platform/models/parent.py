import os
import pandas as pd
from .user import User, Role

class Parent(User):
    def __init__(self, id, full_name, email, password, role: Role):
        super().__init__(id, full_name, email, password, role)
        self.parent_id = id
        self.children = []
    
    def view_child_grades(self, student_id):
        path = 'data/student_assignments.csv'
        if not os.path.exists(path):
            return False

        df = pd.read_csv(path)
        child_grades = df[df['Student ID'] == int(student_id)]
        return child_grades[['Student ID', 'Grade']].to_string(index=False) if not child_grades.empty else 'not found'

    def view_child_assignments(self, student_id):
        path = 'data/student_assignments.csv'
        if not os.path.exists(path):
            return False

        df = pd.read_csv(path)
        child_assignments = df[df['Student ID'] == int(student_id)]
        return child_assignments[['Student ID', 'Content']].to_string(index=False) if not child_assignments.empty else 'not found'
