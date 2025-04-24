from pywebio.input import slider,FLOAT, NUMBER
from pywebio.output import put_html


# HEADER
put_html("<h1>Welcome to our shop</h1>")


# INPUT SECTION

cheese_weight = slider('Cheese', type=FLOAT, min_value=0, max_value=5, value=0.15, required=True)


potato_weight =pw_input("Potato", type=NUMBER, required=True, min=10, value=3)

potato_cost = POTATO_PRICE * potato_weight
cheese_cost = POTATO_PRICE * cheese_weight