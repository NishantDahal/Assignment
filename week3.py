

print("SELECT YOUR ISSUE")
print("'back-pain', 'sore-neck', 'eye-strain', 'fatigue'")
issue_list = []
issue = input("What is your issue? Select from the options above: ")
issue_list.append(issue)

for _ in range(10):
    print("Would you like to add more issues? Enter 1 for 'Yes' or 0 for 'No'")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        issue = input("What else is your issue? Select from the options above: ")
        issue_list.append(issue)
    else:
        break

problems = {
    "start": issue_list,
    "finish": ["not-well"],
    "rules":[
        {
            "issue": "back-pain",
            "solution":"Practice good posture and consider ergonomic adjustments."
        },
        {
            "issue": "sore-neck",
            "solution":"Stretch and rotate your neck regularly, and check your pillow."
        },
        {
            "issue": "eye-strain",
            "solution":"Take regular breaks, follow the 20-20-20 rule, and adjust screen brightness."
        },
        {
            "issue": "fatigue",
            "solution":"Ensure a good sleep routine, stay hydrated, and manage stress."
        },
    ]
}

start = problems['start']
finish = problems['finish']
rules = problems['rules']

for rule in rules:
    if start[0] == rule['issue']:
        print("Solution:", rule['solution'])

