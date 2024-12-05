
my_dict = {
  "students": [
      {"id": 20, "name": "giorgi", "age": 25},
      {"id": 25, "name": "giorgi", "age": 23},
      {"id": 100, "name": "nika", "age": 22},
      {"id": 56, "name": "nika", "age": 25},
      {"id": 1232, "name": "dato", "age": 22},
      {"id": 846723, "name": "archili", "age": 32}
 ] ,
  "subjects": [
      {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
      {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},

      {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
      {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
      {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}}
 ]
}


#for student in my_dict["students"]:
 #   print(student["name"])

#for student in my_dict["students"]:
 #   print(student["age"])

def print_student_ages(data):

    if 'students' in data:
        print("Ages of students:")
        for student in data['students']:

            if 'age' in student:
                print(f"Name: {student['name']}, Age: {student['age']}")
    else:
        print("No students found in the data.")

print_student_ages(my_dict)