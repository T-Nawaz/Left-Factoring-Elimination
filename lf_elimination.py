# Name M. M. Tanzim Nawaz
# ID 1410511642

# Taking input from file and printing the CFG
inputFile = open("CFG_input.txt", "r")
inputString = inputFile.read()
print("*******TEXT INPUT*******\n", inputString, "\n")

# Splitting the CFG into LHS and RHS and printing the output.
LHS_RHS_split = inputString.split("->")

print("*******Left Hand Side*******\n", LHS_RHS_split[0], "\n")

print("*******Right Hand Side*******\n", LHS_RHS_split[1], "\n")

LHS_element = LHS_RHS_split[0].strip(" ")
# Removing any unnecessary whitespace and printing the individual elements of RHS
RHS_elements = LHS_RHS_split[1].split("|")
for i in range(0, len(RHS_elements)):
    RHS_elements[i] = RHS_elements[i].strip(" ")

print("*******Individual Right Hand Side Elements*******\n", RHS_elements, "\n")

common_Terminal = ""
for i in range(0, len(RHS_elements[0])):        # Iterates over the number of chars of the first RHS elements
    for j in range(1, len(RHS_elements)):       # Iterates over the number of individual elements of RHS
        if RHS_elements[0][:i+1] == RHS_elements[j][:i+1]:
            common_Terminal = RHS_elements[0][:i + 1]
            # print("Common element is -", RHS_elements[0][:i+1], "- between -", RHS_elements[0], "and",
            # RHS_elements[j])

new_Non_Terminal = LHS_element + "'"
new_RH_Rule_1 = common_Terminal+new_Non_Terminal
# print(new_Non_Terminal, new_RH_Rule_1)

new_Terminal = {}
for i in range(0, len(RHS_elements)):
    new_Terminal[i] = RHS_elements[i].strip(common_Terminal)
    # print(new_Terminal[i])

new_Production = {}
new_Production[0] = LHS_element + "->" + new_RH_Rule_1
new_Production[1] = new_Non_Terminal + "->"

for i in range(0, len(RHS_elements)):
    new_Production[1] = new_Production[1] + new_Terminal[i] + "|"
new_Production[1] = new_Production[1][:-1]

print("*****OUTPUT*****")
for i in range(0, len(new_Production)):
    print(new_Production[i])