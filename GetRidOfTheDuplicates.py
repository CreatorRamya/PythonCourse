student_date = {'id1':
                {'name': ['Lucy'],
                 'class': ['V'],
                 'subject_integration': ['english, math, science']
                 },

                 'id2':
                {'name': ['Swathi mam'],
                 'class': ['V'],
                 'subject_integration': ['english, math, science']
                 },
}

result = {}

for key, value in student_date.items():
    if value not in result.values():
        result[key] = value

print(result)