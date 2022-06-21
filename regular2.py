import re


with open('text.txt', 'r', encoding='utf-8') as file:
    tex = file.read()


reg1 = r"[А-я]+ [А-я]+" # словосочетание с пробелом
reg2 = r"\w+\d\w+" # слова с цифрой
reg3 = r"\w+\s\w+" # словосочетание с пробелом


reg7 = r"\b[А-Я]{1}[а-я]+\b|\b[а-я]*[А-Я]{1}[а-я]*\b|\b[а-я]*[А-Я]{1}\b" #


see_result = re.findall(reg7, tex)
#print('состоят только из букв', see_result)



reg4 = r"[А-Я]{2,}\w+|\w+\s\w+|\w+\d\w+|\b[а-я]+\b" 
sub_reg = ""
delete_result = re.sub(reg4, sub_reg, tex)
print(delete_result)
