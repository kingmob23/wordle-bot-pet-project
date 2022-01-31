with open('letters.txt', 'r', encoding='utf-8') as ll_freq:  # ll_freq means list of letters sorted by frequency
    ll_freq_content = ll_freq.read()
    # now I will convert the list into a dict by converting the frequency into a weight written in numbers
    l_weight = {}
    weight = 1
    for i in ll_freq_content[::-2]:
        l_weight[i] = weight
        weight += 1

with open('n5.txt', 'r', encoding='Windows-1251') as rus_words_5l:
    list_of_5l_r_w = rus_words_5l.read().split(' ')  # list_of_5l_r_w means list of five - letter Russian words
    list_of_5l_r_w.remove('хи-хи')


def mww(list_of_words, dict_of_letters_with_weight, positions):  # searching for the word with the highest weight
    highest_weight = 0
    word_with_the_most_weight = ''
    for word in list_of_words:
        spell_the_word = [letter for letter in word]
        weight_current_word = 0
        for letter_1 in spell_the_word[positions]:
            weight_current_word += dict_of_letters_with_weight[letter_1]
        if weight_current_word > highest_weight:
            highest_weight = weight_current_word
            word_with_the_most_weight = word
    return word_with_the_most_weight


response = ''  # initialize the variable to which I will transmit the response from the site
while response != 'win':  # the cycle of solving the word game, it is executed until victory
    pos_l_w = slice(0, 5)  # positions of letters whose weight we count
    attempt = mww(list_of_5l_r_w, l_weight, pos_l_w)
    print(attempt, '\n')
    response = input('Что выдало? \n')
    if response == 'nsw':  # nsw means there is no such word
        list_of_5l_r_w.remove(attempt)
    elif response == '50':  # 50 means partial success, part of the letters are correct
        in_correct_pos = input('там, буква позиция \n').split()
        # lay out the letters and their positions separately, then make up a dict
        letters = []
        pos_s = []
        for letter_3 in in_correct_pos[::2]:
            letters.append(letter_3)
        for pos in in_correct_pos[1::2]:
            pos_s.append(pos)
        dict_cor_pos = {}
        for tic in range(len(in_correct_pos) // 2):
            dict_cor_pos[letters[tic]] = int(pos_s[tic])
        poss = []
        for numb in range(5):
            poss.append(numb)
        for key in dict_cor_pos:
            poss.remove(dict_cor_pos[key] - 1)
        pos_l_w = poss
