def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    number_of_words(file_contents)
    letters = letter_distribution(file_contents)
    alphabet = []
    for key in letters:
        if key.isalpha():
            alphabet.append({"letter": key, "occurences": letters[key]})
    alphabet.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_file} ---")
    for a in alphabet:
        var_key = a["letter"]
        var_occurences = a["occurences"]
        print(f"The \'{var_key}\' character was found {var_occurences} times")
    print("--- End report ---")



def number_of_words(string):
    print(len(string.split()))
def letter_distribution(string):
    letters = {}
    for c in string.lower():
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters
def sort_on(dict):
    return dict["occurences"]

main()
