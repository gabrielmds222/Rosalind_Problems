outputFile = []

with open('Python_Village/QuestionFive/rosalind_ini5.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]


with open('Python_Village/QuestionFive/out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))
