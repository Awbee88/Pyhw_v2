# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


with open ('file1.txt', 'w') as file1, open('file2.txt', 'w') as file2:
    txt = 'AAAAAAFDDCCCCCCCAEEEEABC'
    file1.write(txt)
    txt2 = '6A1F2D7C1A4E1A1B1C'
    file2.write(txt2)


# Алгоритм модуля сжатия
def rle_func1(file):
    with open (file, 'r') as f:
        txt = f.read()
    count = 1
    new_txt = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        elif txt[i] != txt[i+1]:
            new_txt += str(count) + txt[i]
            count = 1
    new_txt += str(count) + txt[-1]
    print(new_txt)
    with open ('new_file1.txt', 'w') as n_f1:
        n_f1.write(new_txt)

rle_func1('file1.txt')

# Алгоритм восстановления данных 
def rle_func2(file):
    with open(file, 'r') as f2:
        new_txt = f2.read()
    new_text2 = ''
    for i in range(len(new_txt)):
        if new_txt[i].isdigit():
            temp = int(new_txt[i])
        elif new_txt[i].isalpha():
            new_text2 += temp*new_txt[i]
    print(new_text2)
    with open('new_file2.txt', 'w') as n_f2:
        n_f2.write(new_text2)

rle_func2('file2.txt')



