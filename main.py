word = input("Введите непонятное слово (большими буквами!): ")
meme_dict = {
            "МАПА": "Обычно это слово используют в играх. Мапа - это карта в игре.",
            "ФРАГ": "Фраг - означает убийство в игре которое сделал игрок.",
            "БАГ": "Ошибка в коде игры.",
            "РОФЛ":"В наше время данное слово используют единицы. Рофл - означает шутка.",
            "АГРИТЬСЯ":"Агриться - означает злиться на кого-то.",
            "КРИПОВЫЙ":"Означает страшный или же пугающий.",
            
            }
if word in meme_dict.keys():
		print(meme_dict[word])
else:
    print("Данного слова к сожалению нету в словаре. Но обязательно добавиться!")
