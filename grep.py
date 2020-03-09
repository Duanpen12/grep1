import re
import fileinput
from itertools import islice

def text_file_to_list(file):
    list_of_line = open(file, 'r')
    content = list_of_line.readlines()
    list_of_line.close()
    return content


text_file = 'people.txt'
my_all_file = text_file_to_list(text_file)
print(my_all_file)


# display only the 3rd line from the file people.txt;
f = open('people.txt', 'r')
content = f.readlines()
print("1.", content[2])  # 0,1,2


# insert the text Additional line between lines 2 and 3 in the file cars.txt;
f = open('cars.txt', 'r')
content = f.readlines()
# print(content)
content.insert(2, 'Additional line\n')
file_to_write = open('cars_modified.txt', "w")
file_to_write.writelines(content)
file_to_write.close()
print("2", content)


# display the lines 4-10 from the file people.txt;
f = open('people.txt', 'r')
content = f.readlines()
for line in content[4:11]:
    print("3", line)


# display the file people.txt except the lines 4-10;
# f = open('people.txt', 'r')
# content = f.readlines()




# display from the file people.txt the lines starting with the string Cl;
f = open('people.txt', 'r')
content = f.readlines()
regex_whole_line_having_q = '^Cl\w+'
for line in content:
    line = line.strip()
    line_match = re.search(regex_whole_line_having_q, line)
    if line_match:
        print("4", line)


# display from the file people.txt the lines containing the strings anna or Anna;
f = open('people.txt', 'r')
content = f.readlines()
regex_containing_with_anna_anna = '(\w*anna\w*|\w*Anna\w*)'
for line in content:
    line = line.strip()
    line_match = re.search(regex_containing_with_anna_anna, line)
    if line_match:
        print("5", line)


# replace the name Anna by Anya in the data from the file people.txt ; save the output in the file people2.txt;
f = open('people.txt', 'r')
content_2 = f.readlines()
for line in content_2:
    line = line.replace("Jeremy", "Duanpen")
    # print(line)
    save_file = open('duanpen.txt', "w")
    save_file.writelines(line)
    save_file.close()
    print("6", line)


# replace the string Jo by the string Joel in the data from the file people.txt;
f = open('people.txt', 'r')
content_2 = f.readlines()
for line in content_2:
    line = line.replace('Jo', 'Joel')
    print("7", line)


# display from the file people.txt the surnames of all people;
f = open('people.txt', 'r')
content_3 = f.readlines()
for line in content_3:
    line = line.strip()
    line_surname = line.split(", ")[0]
    new_line = line_surname.split()
    name = new_line[0]
    surname = new_line[-1]
    print("8. Surname ===> ", surname)


# all lines that contain the letter f;
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
# print(content_cars)
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'\w*.*[F|f].*\w*', line)
    if line_match:
        print('\t9.', line_match.group(0))


# all lines which contain the letter f or the letter F;
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'\w*.*[F|f].*\w*', line)
    if line_match:
        print("10", line_match.group(0))


# all lines that contain the letter r (including line numbers);
cars = open('cars.txt', 'r')
content_cars1 = cars.readlines()
for index in range(0, len(content_cars1)):
    line = content_cars1[index].strip()
    line_match = re.search(r'(\w*.*r.*\w*)', line)
    if line_match:
        print('\t 11. including number ===> ', index + 1, line_match.group(0))


# all lines that contain car names beginning with the letter F
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'.*^[F].*\w+', line)
    if line_match:
        print("12", line_match.group(0))


# the number of lines that contain car names ending with the letter t;
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
# cars_ending_with_t = []
for index in range(0, len(content_cars)):
    line = content_cars[index].strip()
    car_name = line.split()[0]
    if car_name.endswith("t"):
        # cars_ending_with_t.append(line)
        print('\t 13. the number of lines that contain car names ending with the letter t => ', index + 1, car_name, line)


# all lines that do not contain the letter k or the letter K
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
# all_line_donot_cars = []
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'\w*^[^k|K]*$\w*', line)
    if line_match:
        # all_line_donot_cars.append(line)
        print("14", line_match.group(0))


# the number of car names that do not contain the letter p at the second place
cars = open('cars.txt', 'r')
content_cars = cars.readlines()
# number_cars = []
for index in range(0, len(content_cars)):
    line = content_cars[index].strip()
    name_second = line.split()[0]
    line_match = re.search(r'\w*^[^P|p]*$\w*', name_second)
    if line_match:
        print("\t 15.", index + 1, "= ", line_match.group(0), "     =", line)


# all lines that contain the string Anna (case insensitive);
people = open("people.txt", "r")
content_people = people.readlines()
# line_of_number = []
for index in range(0, len(content_people)):
    line = content_people[index].strip()
    line_match = re.search(r'\w*.*(anna|Anna).*\w*', line)
    if line_match:
        # line_of_number.append(line)
        print("16. all lines that contain the string Anna (case insensitive) : ", index + 1, line_match.group(0), line)


# details of all people named Anna;
people = open("people.txt", "r")
content_cars = people.readlines()
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'\w*.*Anna.*\w*', line)
    if line_match:
        print('\t17.', line_match.group(0))


# details of all people named Thomas
cars = open("people.txt", "r")
content_cars = cars.readlines()
for line in content_cars:
    line = line.strip()
    all_list_name_surname = line.split(',')[0]
    name_surname = all_list_name_surname.split()
    name = name_surname[0]
    line_match = re.search(r'\w*.*Thomas.*\w*', name)
    if line_match:
        print('18. Thomas = ', line_match.group(0), line)


# details of all people named Maria or Jhon
cars = open("people.txt", "r")
content_cars = cars.readlines()
for line in content_cars:
    line = line.strip()
    line_match = re.search(r'\w*(.*Maria.*|.*Jhon.*)\w*', line)
    if line_match:
        print('19. \t', line_match.group(0))


# the number of people whose surnames begin with the string Jh;
people = open("people.txt", "r")
content_people = people.readlines()
for index in range(0, len(content_cars)):
    line = content_people[index].strip()
    surname_begin = line.split(",")[0]
    surname = surname_begin.split()
    surname_start_with_jh = surname[-1]
    line_match = re.search(r'.*^Jh.*\w+', surname_start_with_jh)
    if line_match:
        # number_of_line.append(line)
        print("20", index + 1, line_match.group(0), line)


# data of all people whose name is consisted of 5 letters;
cars = open('cars.txt', 'r')
content_car = cars.readlines()
for line in content_car:
    line = line.strip()
    line_name = line.split(",")[0]
    name_surname = line_name.split()
    name = name_surname[0]
    line_match = re.search(r'\b\w{5}\b', name)
    if line_match:
        print('21. \t', line_match.group(), "==>", line)



# data of all people whose names end with the letter a;
cars = open('cars.txt', 'r')
content_car = cars.readlines()
for line in content_car:
    line = line.strip()
    line_match_name = line.split(",")[0]
    name_list = line_match_name.split()
    name_list = name_list[0]
    if name_list.endswith("a"):
        print("22", line)


# data on all people whose names end with the letter a and with surnames
# beginning with the letter J;
f = open('people.txt', 'r')
content = f.readlines()
count = 0
for line in content:
    line = line.strip()
    name_and_surname = line.split(",")[0]
    name_surname_list = name_and_surname.split()
    name = name_surname_list[0]
    surname = name_surname_list[-1]
    if name.endswith("a") and surname.startswith("J"):
        print('23. \t', line)


# all lines related to users with logins starting with ag, ak or ar;
etc_passwd = open('/etc/passwd', "r")
content = etc_passwd.readlines()
# print(content)
for index in content:
    index = index.strip()
    # logins_start = re.search(r'^.*[a|k].*\w+', index)
    if index.startswith("a"):
        print("24", index)


# all lines for users with logins that do not begin with the string da;   line_match = re.search(r'\w*^[^a]*$\w*', line)
# save the data in the file called da.txt in the home directory;
etc_passwd = open('/etc/passwd', "r")
content = etc_passwd.readlines()
for index in content:
    index = index.strip()
    logins_not_being_with_da = re.search(r'\w*^[^da]*$\w*', index)
    file_to_write = open('da.txt', "w")
    file_to_write.writelines(index)
    file_to_write.close()
    if logins_not_being_with_da:
        print("25. \t", logins_not_being_with_da.group(0))


# all lines related to users named Piotr (with the line numbers);
etc_passwd = open('/etc/passwd', "r")
content = etc_passwd.readlines()
for index in range(0, len(content)):
    line = content[index].strip()
    # print(index + 1, line)
    users_name = line.split(':')[0]
    name_line = users_name.split()
    # print(name_line)
    users = name_line[0]
    # print(index + 1, users)
    line_name_piotr = re.search(r'\w*(.*ning.*)\w*', users)
    if line_name_piotr:
        print("26", index + 1, line_name_piotr.group(0), line)


# the number of users named Adam.
etc_passwd = open('/etc/passwd', "r")
content = etc_passwd.readlines()
for index in range(0, len(content)):
    number = content[index].strip()
    list_users_name = number.split(':')[0]
    name_users = list_users_name.split()
    name = name_users[0]
    # print(name)
    name_adam = re.search(r'\w*(.*saned.*)\w*', name)
    if name_adam:
        print("27", index + 1, name_adam.group(0), number)


# In the home directory, create the file text_grep.txt with the following content:
new_text_file = open('text_grep.txt', "w+")
new_text_file.write("""A file called * text_grep.txt *.
Strange text file?
Nothing unusual! A few sentences (?) To test the grep filter.
:-)

After the empty line we have a poem without a dot (yes, yes)
We now give 4 characters {+, *, 0, ^} in curly brackets.

There is no dot again, but we have the numbers: 3, 6, 8, 9
What_else? ***

Maybe the email address: my@inbox.net.pl
What next?
{End!!!}
""")
new_text_file.close()


# From the file text_grep.txt display:
# a) lines that contain the letter n or the letter N;
# b) lines that start with the letter W;
# c) lines that contain numbers;
# d) lines that contain a question mark;
# e) lines that contain a question mark or asterisk;
# f) number of empty lines;
# g) lines that do not contain spaces;
# h) lines that do not contain dots; save these lines in the file called no_dot.txt;
# i) lines that contain round brackets: (or);
# j) lines that contain curly braces: {or}.



# a) lines that contain the letter n or the letter N;
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    line_match = re.search(r"\w*.*(N|n).*\w*", index)
    if line_match:
        print("29", line_match.group(0))


# b) lines that start with the letter W;
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    if index.startswith("W"):
        print("30", index)


# c) lines that contain numbers;
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in range(0, len(content)):
    line = content[index]
    print("31", index + 1, line)


# d) lines that contain a question mark;
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    content_a_question_mark = re.search(r"\w*.*[?].*\w*", index)
    if content_a_question_mark:
        print("32", content_a_question_mark.group())


# e) lines that contain a question mark or asterisk
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    content_a_question_mark = re.search(r"\w*.*[?|*].*\w*", index)
    if content_a_question_mark:
        print("33", content_a_question_mark.group())


# f) number of empty lines;
# g) lines that do not contain spaces;
# h) lines that do not contain dots; save these lines in the file called no_dot.txt;
# i) lines that contain round brackets: (or);
# j) lines that contain curly braces: {or}.
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
content.insert(4, '\n')
# print(content)
for index in range(0, len(content)):
    line = content[index]
    if line in ['\n', '\r\n']:
        print("34", index + 1, line)


# g) lines that do not contain spaces;  /^(?!PART)/
# h) lines that do not contain dots; save these lines in the file called no_dot.txt;
# i) lines that contain round brackets: (or);
# j) lines that contain curly braces: {or}.
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    line_match = re.search(r"^[^ ]+$", index)
    if line_match:
        print("\t35. ", line_match.group(0))


# h) lines that do not contain dots; save these lines in the file called no_dot.txt;
# i) lines that contain round brackets: (or);
# j) lines that contain curly braces: {or}.
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    line_match = re.search(r"^[^.]+$", index)
    new_text_file = open('no_dot.txt', "w")
    new_text_file.writelines(index)
    new_text_file.close()
    if line_match:
        print("36", line_match.group())


# i) lines that contain round brackets: (or);
# j) lines that contain curly braces: {or}.
text_grep = open('text_grep.txt', "r")
content = text_grep.readlines()
for index in content:
    index = index.strip()
    line_match = re.search(r".*\{(.*?)\}.*|.*\((.*?)\).*", index)
    if line_match:
        print("\t37. ", line_match.group(0))










