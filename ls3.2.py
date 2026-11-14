student = {
    "name": "Али",
    "age": 13,
    "city": "Бишкек",
    "language": "Python"
}

print(student)
student["age"] = 14
student["grade"] = 5
del student["city"]
print(student)
for key, value in student.items():
    print(key, " - ", value)