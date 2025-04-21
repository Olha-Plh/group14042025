# print(id("jenjnnn"))


some_string = "jenjnnn23 \U00002763"
some_string = "jenjnnn23 \n \U00002763"
print(some_string)

pos_number_of_a = ord("a")
print(pos_number_of_a)


char_97 = chr(97)
print(char_97)

print(f"{char_97=}")
formatted_string = f"{char_97=}"
formatted_string = f"{char_97=} but {pos_number_of_a}"
print(formatted_string)

pass


name = "Kate"
service = "Dentist"
address = "Beautiful, 17"
# sms = name + service + address
# sms = "Dear" + name + ", we're waiting for you on " + service + "our address:" + address )
sms = f"Dear {name}, we are waiting for you on {service}. Our address: {address}"
