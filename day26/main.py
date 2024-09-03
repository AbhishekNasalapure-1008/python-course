import pandas

data=pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)

def generate_phonetics():
    word=input("Enter text to convert to NATO alphabet\n").upper()
    try:
        result=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetics()
    else:
        print(result)

generate_phonetics()

