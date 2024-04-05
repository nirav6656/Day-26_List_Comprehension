# Square of numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [n**2 for n in numbers]
#
# print(squared_numbers)

# -------------------------------------------------
# FILTERING EVEN NUMBERS

# list_of_strings = input().split(',')
#
# list_of_numbers = [int(n) for n in list_of_strings]
# result = [n for n in list_of_numbers if n % 2 == 0]
# print(result)

# -------------------------------------------------
# DATA OVERLAP

# data1 = open(file="file1.txt").read()
# data2 = open(file="file2.txt").read()
#
# data1_list = data1.split("\n")
# data2_list = data2.split("\n")
#
#
# result = [int(n) for n in data1_list if n in data2_list]
# print(result)

# -------------------------------------------------
# DICTIONARY COMPREHENSION 1

# sentence = input()
# sentence_list = sentence.split()
#
# result = {n: len(n) for n in sentence_list}
#
# print(result)


# -------------------------------------------------
# DICTIONARY COMPREHENSION 2

# weather_c = (eval(input()))
#
#
# weather_f = {key: (item * (9 / 5)) + 32 for (key, item) in weather_c.items()}
#
# print(weather_f)

# -------------------------------------------------
# Pandas Dataframe

# student_dict = {
#     "student" : ["nik","radha","james","lily"],
#     "score" : [56,76,98,45]
# }
#
# import pandas
# student_data_frames = pandas.DataFrame(student_dict)
#
# for (index,row) in student_data_frames.iterrows():
#     print(row.score)

# -------------------------------------------------
# NATO Alphabet Project

import pandas

# TODO 1. Create a dictionary in this format:
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in pandas.DataFrame(nato).iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the name").upper()
user_output = [nato_dict[letter] for letter in user_input]
print(user_output)
