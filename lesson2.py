import les2_constants

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




name = "Kate"
service = "Dentist"
# sms = name + service + address
# sms = "Dear" + name + ", we're waiting for you on " + service + "our address:" + address )
sms1 = f"Dear {name}, we are waiting for you on '{service}'. Our address: {les2_constants.address}"


print(sms1)


MSG_ENTER_NAME = 'Your name:'
name = input(MSG_ENTER_NAME)



SMS_TEMPLATE = ("Dear {name}, we are waiting for you on {service}. Our address: {address}")
sms2 = SMS_TEMPLATE.format(name=name, service='Manicure', address=les2_constants.address)
print(f"{sms2=}")





pass
