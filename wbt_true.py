with open('letters.txt', 'r', encoding='utf-8') as letters_by_frequency:
    content = letters_by_frequency.read()
    letters_with_weight = {}
    weight = 1
    for c in content[::-2]:
        letters_with_weight[c] = weight
        weight += 1

with open('n5.txt', 'r', encoding='Windows-1251') as five_letter_words_obj:
    five_letter_words = five_letter_words_obj.read().split()
    five_letter_words.remove('хи-хи')


def weighing(spell, weighted_letters, calculating_this):
    weight_of_the_current_word = 0
    for p in calculating_this:
        letter = spell[p]
        weight_of_the_current_word += weighted_letters[letter]

    return weight_of_the_current_word


def letters_are_in_place():
    return 'функция пока не готова'


def search_for_a_word(list_of_words, must_not_contain):
    highest_weight = 0
    most_weighty_word = ''

    for w in list_of_words:
        spell_the_word = [letter for letter in w]

        check = False
        for s in spell_the_word:
            if s in must_not_contain:
                check = True
        if check:
            continue

        current_weight = weighing(spell_the_word, letters_with_weight, here_we_count)

        if current_weight > highest_weight:
            highest_weight = current_weight
            most_weighty_word = w

    return most_weighty_word


def partial_success():
    missing_letters = input('нету \n').split()
    guessed_letters_input = input('там, буква позиция \n').split()
    letters = []
    positions = []
    for p in guessed_letters_input[::2]:
        letters.append(p)
    for i in guessed_letters_input[1::2]:
        positions.append(int(i) - 1)
    guessed_letters = {}
    for d in range(len(guessed_letters_input) - 1):
        guessed_letters[letters[d]] = positions[d]

    counting_positions = []
    for o in range(5):
        counting_positions.append(o)
    for r in guessed_letters:
        counting_positions.remove(guessed_letters[r])

    return missing_letters, counting_positions, guessed_letters


response = ''
letters_that_are_not_there = []
here_we_count = list(range(5))
while response != 'win':
    attempt = search_for_a_word(five_letter_words, letters_that_are_not_there)
    five_letter_words.remove(attempt)
    print(attempt, '\n')
    response = input('Что выдало? \n')

    if response == 'nsw':  # nsw means there is no such word
        print('ПУКНИ В ЛУЖУ')
        # with open('n5.txt', 'rw', encoding='Windows-1251') as file:
        #     content_2 = file.read()
        #     content_2.remove(attempt)
    elif response == '50':  # 50 means partial success, part of the letters are correct
        letters_that_are_not_there, here_we_count, good_letters = partial_success()

print('конграц!')
