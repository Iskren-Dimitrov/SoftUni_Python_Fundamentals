company_id = input()
dictionaries = {}

while company_id != "End":
    current_command = company_id.split(" -> ")
    company_name = current_command[0]
    id = current_command[1]
    if company_name not in dictionaries.keys():
        dictionaries[company_name] = []
    dictionaries[company_name].append(f"-- {id}")
    company_id = input()

for company in dictionaries.keys():
    print(f"{company}")
    for ids in dict.fromkeys(dictionaries[company]):
        print(f"{ids}")

