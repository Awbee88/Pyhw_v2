# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = 'Абрам абв изуабвчал алфаабвфит по абвгдейке'

def delete_word(text):
    text_list = text.lower().split(' ')
    for i in range(0, len(text_list)):
        if 'абв' in text_list[i]:
            text_list[i] = text_list[i].replace('абв', '')
    if '' in text_list:
        text_list.remove('')        
    
    return ' '.join(text_list).capitalize()


print(f'Исходная строка: "{words}" \nСтрока после удаления \'абв\': "{delete_word(words)}"')

