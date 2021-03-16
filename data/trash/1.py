import re
import sqlite3

id = 1
with open('1.txt', encoding='utf-8') as file:
    lst = '\n'.join(file.readlines())

con = sqlite3.connect('../sql/test.db')
cur = con.cursor()

for quest in lst.split(' '):
    dct = {
        'Глава': None,
        "Вопрос": None,
        "Ответ1": None,
        "Ответ2": None,
        "Ответ3": None,
        "Ответ4": None,
        "Поясн": None,
        'Правильный ответ': None
    }
    for line in quest.split('\n'):
        text = re.sub(r'\s+', ' ', line.strip())
        if not text:
            continue
        if dct['Глава'] and dct['Вопрос'] and dct['Ответ1'] and dct['Ответ2'] and dct['Ответ3'] and type(dct['Ответ4']) is str :
            if dct['Поясн'] is None:
                dct['Поясн'] = ''
            dct['Поясн'] += text
            continue
        if 'Задача' in text:
            text = line.strip()[7:]
            dct['Глава'] = text.split('.')[0]
            quest = ''
        if dct['Глава'] and not dct["Ответ1"]:
            if not text[0].isdigit():
                quest += text + '\n'
                continue
            else:
                dct['Вопрос'] = quest
                ans = ''
        if dct['Вопрос'] and not dct["Ответ2"]:
            if text[0] != '2':
                dct['Ответ1'] = True
                ans += text.replace('1)', '') + '\n'
                continue
            else:
                dct['Ответ1'] = ans
                ans = ''
        if dct['Ответ1'] and not dct["Ответ3"]:
            if text[0] != '3':
                dct['Ответ2'] = True
                ans += text.replace('2)', '') + '\n'
                continue
            else:
                dct['Ответ2'] = ans
                ans = ''
        if dct['Ответ2'] and not dct["Ответ4"]:
            if text[0] != '4':
                dct['Ответ3'] = True
                ans += text.replace('3)', '') + '\n'
                continue
            else:
                dct['Ответ3'] = ans
                ans = ''
        if dct['Ответ3'] and not dct["Поясн"]:
            if type(dct['Ответ4']) is not str:
                if text[0] != 'П':
                    dct['Ответ4'] = True
                    ans += text.replace('4)', '') + '\n'
                    continue
                else:
                    dct['Ответ4'] = ans
                    ans = ''
                    dct['Поясн'] = text
    else:
        for i in dct['Поясн'][::-1]:
            if i.isdigit():
                dct['Правильный ответ'] = int(i)
                break
        dct['Поясн'] = dct['Поясн'][:-9]
        print(dct)
        cur.execute(f'''INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (id, dct['Глава'], dct['Вопрос'], dct['Ответ1'], dct['Ответ2'], dct['Ответ3'], dct['Ответ4'], dct['Правильный ответ'], dct['Поясн']))
        con.commit()



