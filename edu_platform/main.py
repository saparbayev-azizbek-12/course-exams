from models.user import Role
from models.student import Student
from models.teacher import Teacher
from models.parent import Parent
from models.admin import Admin

#demo users
admin = Admin(1, "Admin", "admin@edu.com", "adminpass", Role.ADMIN)
teacher = Teacher(2, "Teacher", "teacher@edu.com", "teacherpass", Role.TEACHER)
student = Student(3, "Student", "student@edu.com", "studentpass", Role.STUDENT, 5)
parent = Parent(4, "Parent", "parent@edu.com", "parentpass", Role.PARENT)

def _admin():
    print()
    actions = ["Foydalanuvchi qo'shish", "Foydalanuvchi o'chirish", "Foydalanuvchilar ro'yxatini ko'rish"]
    for i, a in enumerate(actions, 1):
        print(f"{i}. {a}")
    act = input("Admin vazifasini tanlang: ").strip()
    if act == "1":
        full_name = input("Ism Familya: ")
        email = input("Email: ")
        password = input("Parol: ")
        print("Rolni tanlang: (1-Admin, 2-Teacher, 3-Student, 4-Parent)")
        r_idx = int(input("Raqam: "))-1
        res = admin.add_user(full_name, email, password, r_idx)
        if res:
            print(res)
        else:
            print("Xatolik yuz berdi!")
    elif act == "2":
        uid = input("O'chiriladigan foydalanuvchi ID: ")
        if admin.remove_user(int(uid)):
            print("O'chirildi!")
        else:
            print("Topilmadi!")
    elif act == "3":
        print(admin.generate_report())
    else:
        print("Noto'g'ri tanlov!")

def _teacher():
    print()
    actions = ["Assignment yaratish", "Assignment baholash", "O'quvchi javoblarini ko'rish"]
    for i, a in enumerate(actions, 1):
        print(f"{i}. {a}")
    act = input("Teacher vazifasini tanlang: ").strip()
    if act == "1":
        content = input("Assignment mazmuni: ")
        if teacher.create_assignment(content):
            print("Assignment yaratildi!")
    elif act == "2":
        aid = int(input("Assignment ID: "))
        grade = int(input("Bahosi: "))
        print(teacher.grade_assignment(aid, grade))
    elif act == "3":
        sid = int(input("O'quvchi ID: "))
        print(teacher.view_student_assignments(sid))
    else:
        print("Noto'g'ri tanlov!")

def _student():
    print()
    actions = ["Assignment ko'rish", "Assignment topshirish", "Baho ko'rish"]
    for i, a in enumerate(actions, 1):
        print(f"{i}. {a}")
    act = input("Student vazifasini tanlang: ").strip()
    if act == "1":
        print(student.view_assignments())
    elif act == "2":
        aid = int(input("Assignment ID: "))
        content = input("Topshiriq javobi: ")
        print(student.submit_assignment(aid, content))
    elif act == "3":
        print(student.view_grades())
    else:
        print("Noto'g'ri tanlov!")

def _parent():
    print()
    actions = ["Farzand baholari", "Farzand topshiriqlari"]
    for i, a in enumerate(actions, 1):
        print(f"{i}. {a}")
    act = input("Parent vazifasini tanlang: ").strip()
    if act == "1":
        sid = input("Farzand ID: ")
        print(parent.view_child_grades(sid))
    elif act == "2":
        sid = input("Farzand ID: ")
        print(parent.view_child_assignments(sid))
    else:
        print("Noto'g'ri tanlov!")

def main():
    while True:
        print("\nTanlang:")
        choices = ["Admin", "Teacher", "Student", "Parent", "Chiqish"]
        for i, r in enumerate(choices, 1):
            print(f"{i}. {r.title()}")
        print()
        choice = input("Raqamni kiriting: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Noto'g'ri tanlov!")
            return
        choice = int(choice)

        if choice == 1:
            _admin()

        elif choice == 2:
            _teacher()

        elif choice == 3:
            _student()

        elif choice == 4:
            _parent()

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
