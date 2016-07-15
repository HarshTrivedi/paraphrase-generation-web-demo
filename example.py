from main_lib import *


list_of_sentences = [
"At least 12 people were killed in the battle last week",
"At least 12 people lost their lives in last week's fighting",
"Last week's fight took at least 12 lives",
"The fighting last week killed at least 12",
"The battle of last week killed at least 12 persons",
"At least 12 persons died in the fighting last week",
"At least 12 died in the battle last week",
"At least 12 people were killed in the fighting last week",
"During last week's fighting, at least 12 people died",
"Last week at least twelve people died in the fighting",
"Last week's fighting took the lives of twelve people"

]


fsm_code = get_fsm_code(list_of_sentences)
# returns graphviz code for generated fsm


get_svg( fsm_code.strip() )
# generates svg for the graphviz code