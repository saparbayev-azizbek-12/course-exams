import os
import pandas as pd
from .user import User, Role

class Teacher(User):
    def __init__(self, id, full_name, email, password, role: Role):
        super().__init__(id, full_name, email, password, role)
        self.teacher_id = id
        self.subjects = []
        self.classes = []
        self.assignments = {}

    def create_assignment(self, content):
        path = 'data/assignments.csv'
        if os.path.exists(path):
            df = pd.read_csv(path)
            new_id = df['ID'].max() + 1
        else:
            df = pd.DataFrame(columns=['ID', 'Content'])
            new_id = 1

        df.loc[len(df)] = [new_id, content]
        df.to_csv(path, index=False)
        return True
        
    def grade_assignment(self, assignment_id, grade):
        path = 'data/student_assignments.csv'
        if not os.path.exists(path):
            return False

        df = pd.read_csv(path)
        if assignment_id not in df['Assignment ID'].values:
            return False
        
        df.loc[df['Assignment ID'] == assignment_id, 'Grade'] = grade
        df.to_csv(path, index=False)
        return True
    
    def view_student_assignments(self, student_id):
        if not os.path.exists('data/student_assignments.csv'):
            return False

        df = pd.read_csv('data/student_assignments.csv').to_string(index=False)
        student_assignments = df[df['Student ID'] == student_id]
        return student_assignments if not student_assignments.empty else 'not found'