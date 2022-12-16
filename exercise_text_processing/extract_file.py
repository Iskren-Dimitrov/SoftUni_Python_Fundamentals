string = input().split("\\")

current_element = string[-1].split(".")
file_name = current_element[0]
file_extension = current_element[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
