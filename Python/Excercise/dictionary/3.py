employees = {
    'employee1': {'name': 'Alice', 'age': 30, 'salary': 50000},
    'employee2': {'name': 'Bob', 'age': 25, 'salary': 45000},
    'employee3': {'name': 'Charlie', 'age': 35, 'salary': 60000}
}
for i,details in employees.items():
    details['salary'] = details['salary'] * 0.1 + details['salary']


# print(employees.items())

print(employees)