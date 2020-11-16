from itertools import permutations
given_word="OBANWRI"
letter_list=[','.join(letter) for letter in given_word]

word_combinations ={''.join(p) for p in permutations(letter_list)}

for word in word_combinations:
    if word=='RAINBOW':
        print(word,"is a correct english word.")
        


'''
code to put each line of a for loop into a file.
outF = open("myOutFile.txt", "w")
for word in perms:
  # write line to output file
  outF.write(word)
  outF.write("\n")
outF.close()
'''
