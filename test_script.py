from main_lib import *


list_of_sentences = [
# "Last week's fight took at least 12 lives",
# "During last week's fighting, at least 12 people died"
"Last week's fighting took the lives of twelve people",
"Last week's fight took at least 12 lives",
"The battle of last week killed at least 12 persons",
"The fighting last week killed at least 12",

# "Last week at least twelve people died in the fighting"

]

# list_of_sentences = [
# 	"At least 12 persons died in the fighting last week",
# 	"At least 12 people were killed in the fighting last week",
# 	"At least 12 people were killed in the battle last week"
# ]


fsm_code = get_fsm_code(list_of_sentences)


# print fsm_code
# print get_svg( fsm_code.strip() )