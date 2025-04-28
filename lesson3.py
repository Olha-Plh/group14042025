some_string = "am\n5     my name is Igor LLLLL 82872728 namer"


#
# upper = some_string.upper()
# lower = some_string.lower()
# title = some_string.title()
# capitalize = some_string.capitalize()
# chain = some_string.lower().upper().capitalize()
#
# clear_string_spaces = some_string.strip()
# clear_string_symbols = some_string.strip(" 54namE")
# clear_string_symbols_left = some_string.lstrip(" 54namE")
# clear_string_symbols_right = some_string.rstrip(" 54namE")
#
# change_inner_text = (
#     some_string.replace("name", "surname", 1)
#     .replace("Igor", "igor")
#     .replace("namer", "")
#     .replace("8", "7")
# )
#
# table = str.maketrans("78", "87", "\n")
# result_smart_change = some_string.translate(table)


slices1 = some_string[:]
slices2 = some_string[0:12]
slices3 = some_string[12:20]
slices4 = some_string[::2]
slices5 = some_string[1:25:2]
slices6 = some_string[::-1]  # reverse
slices7 = some_string[::-2]  # reverse
slices8 = some_string[-3:-20:-2]  # reverse


pass
