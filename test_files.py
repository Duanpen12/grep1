def list_from_file(file):
    open_text = open(file, 'r')
    content = open_text.readlines()
    open_text.close()
    return content


text_file_cars = 'cars.txt'
print_list_from_file = list_from_file(text_file_cars)
print(print_list_from_file)


text_file_people = 'people.txt'
print_list_from_file_people = list_from_file(text_file_people)
print(print_list_from_file_people)


print_list_from_file.insert(2, 'Duanpen \n')     # how to insert the line at the file
print(print_list_from_file)

print_list_from_file_people.insert(1, "     \n")
print(print_list_from_file_people)


# how to save file in Python
print_list_from_file_people.insert(1, "     \n")
files_to_write = open('new_people.txt', 'w')
files_to_write.writelines(print_list_from_file_people)
files_to_write.close()
print(print_list_from_file_people)


def add(a, b):
    """ 1234567890 """
    return a + b


print(add.__doc__)

