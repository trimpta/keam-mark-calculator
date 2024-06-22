import re
from answer_key import *

with open("response.txt") as rizz:
    brainrot = rizz.readlines()[11:]
    gyatt = []
    for i in brainrot:
        if i[0] != "Q":

            gyatt.append(i.lstrip())

    

    gyatt =  "".join(gyatt)

    ohio = []

    for i in re.findall(r'[ABCDE]|NA', gyatt):
        ohio.append(i.lstrip())


sc = 0


sigmarizz = input("Exam on (5/6/7/8/9) :")
skibidi = int(input("Enter Physics + Chemistry + Maths mark out of 300 :"))


if len(ohio) != len(keys[sigmarizz]):
    raise InterruptedError(f"Error. Try again, {len(ohio)} != {len(keys[sigmarizz])}")

for i, j in zip(ohio, keys[sigmarizz]):

    if i == "NA":
        continue 
    
    if i == j:
        sc += 4
    else:
        sc -=1

print(f"{150 - len(keys[sigmarizz])} Questions Cancelled.")
print(f"{sc} marks out of {len(keys[sigmarizz])*4} in keam")
print(f"total marks: {sc/2 + skibidi} out of {(300 + len(keys[sigmarizz])*2)}")