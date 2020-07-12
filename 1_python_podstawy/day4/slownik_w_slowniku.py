"""
uczeń:
    - lista obecnośco
    - przedmiot: oceny
"""

def add_new_student(name):
    new_student = {"obecnosc": [], "przedmioty": {}}
    school[name] = new_student

def add_subject(subject):
    for key in school:
        school[key]["przedmioty"][subject] = []

def add_mark(name, subject, mark):
    school[name]["przedmioty"][subject].append(mark)

school = {}
add_new_student("Kate")
add_new_student("Mark")

school["Kate"]["obecnosc"].append("20.04")

add_subject("matma")

add_mark("Kate", "matma", 6)

add_mark("Kate", "matma", 7)
print(school)


for key, value in school.items():
    print(key, value)