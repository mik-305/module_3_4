def single_root_words(root_word, *other_words):
    same_words = []  # Список слов, содержащих искомое(изначально пустой)
    root_word = root_word.upper()  # Искомое слово в верхний регистр(для поиска)
    spisok_param = other_words
    for i in spisok_param:
        if root_word in i.upper() or i.upper() in root_word:  # Если искомое слово есть(с учётом ИЛИ)
            same_words.append(i)  #  заносим в список слово, содержащее искомое
    print(same_words)

print('---Обязательное слово в произв.пареметрах---- ')
single_root_words('дуб', 'Дубрава', 'ОгорОд', 'поДдубный', 'ЗадуБевший')
print('---Слова из произв.пареметров в обязательное слове ---- ')
single_root_words('жеЛезныЙ', 'мЕдный', 'желЕ', 'кашА', 'железный АРГУМЕНТ')

