# Recitation Activity #8
# You must submit your file by the end of the allocated period for submissiom
#
# General Instructions
#  - Do NOT change the function name
#  - Replace  "ans1" with the passcode provided during your recitation. Do not remove the quotes
#  - Enter your final answer in the bubblePass dictionary, the key is the pass number and
#    the value the current state of the list after that pass. For example for te list [12, 35, 5, 42, 77, 101]
#    bubblePass ={1:[12, 5, 35, 42, 77, 101], 2:[5, 12, 35, 42, 77, 101], 3:[5, 12, 35, 42, 77, 101]}


def answers():
    # Activity answers

    passcode = "443rt"

    bubblePass ={1:[3, 5, 9, 1, 22, 16, 4, 23],
    2:[3, 5, 1, 9, 16, 4, 22, 23],
    3:[3, 1, 5, 9, 4, 16, 22, 23],
    4:[1, 3, 5, 4, 9, 16, 22, 23],
    5:[1, 3, 4, 5, 9, 16, 22, 23],
    6:[1, 3, 4, 5, 9, 16, 22, 23]}

    # Do not modify the return statement
    return passcode, bubblePass
