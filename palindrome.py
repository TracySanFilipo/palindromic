def refine(messy_sentence):
    if len(messy_sentence) == 0:
            return ""
    else:
        if messy_sentence[0].isalpha() == True:
            phrase_given_letters = messy_sentence[0] + refine(messy_sentence[1:])
        else:
            phrase_given_letters = refine(messy_sentence[1:])
    phrase_given_refined = phrase_given_letters.lower()
    return phrase_given_refined

def forward(phrase_of_letters):
    if len(phrase_of_letters) == 0:
        return ""
    else:
        return phrase_of_letters[0] + forward(phrase_of_letters[1:])

def backward(phrase_of_letters2):
    if len(phrase_of_letters2) == 0:
        return ""
    else:
        return backward(phrase_of_letters2[1:]) + phrase_of_letters2[0]

def is_palindrome(phrase_to_evaluate):
    phrase_given_refined = refine(phrase_to_evaluate)
    print(phrase_given_refined)
    one_direction = forward(phrase_given_refined)
    print(one_direction)
    other_direction = backward(phrase_given_refined)
    print(other_direction)
    if one_direction == other_direction:
        print("is a palindrome")
        return True
    else:
        print("is not a palindrome")
        return False

def main():
    phrase_given = input("Please give me a sentence or phrase: ")
    print(phrase_given)
    is_palindrome(phrase_given)
    return

main()
