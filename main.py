from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

text = []
second_text = []

def info_correct():
    for t in contacts_list:
        t = ','.join(t)
        pattern = re.compile(
            r"(\w+)[\s,](\w+)[\s|,]?(\w+)?,(,{1,2})?(\w+)?([,]{1,2})?(\w+[^0-9+,]*)?,(\w*|(\+7|8)([ \(]*)?(\d{3})[- \)]*(\d{3})[- \)]*(\d{2})[- \)]*(\d{2})([ \(]*)?(доб.)?( )?(\d*)?)[\,)],?([\S*\(\)]*)")
        result = pattern.sub(r"\1,\2,\3,\5,\7,\8,\19", t)
        text.append([result])

def phone_correct():
    for t_2 in text:
        t_2 = ','.join(t_2)
        pattern_2 = re.compile(
            r"(\+7|8)([ \(]*)?(\d{3})[- \)]*(\d{3})[- \)]*(\d{2})[- \)]*(\d{2})([ \(]*)?(доб.)?( )?(\d*)?")
        result_2 = pattern_2.sub(r"+7(\3)\4\5\6 \8\10", t_2)
        second_text.append([result_2])




def write(info):
    with open("phonebook.csv", "w", newline='') as f:
        datawriter = csv.writer(f, delimiter='"', quoting=csv.QUOTE_NONE)
        for item in info:
            datawriter.writerows([item])


def no_double(file):
    with open(file) as g:
        rows = csv.reader(g, delimiter=",")
        contacts_list_2 = list(rows)
    dir_1 = []
    dir_2 = []
    for item in contacts_list_2:
        dir_list = {f'{item[0]}, {item[1]}': item[2:]}
        if dir_list.keys() not in [d.keys() for d in dir_1]:
            dir_1.append(dir_list)
        else:
            for d in dir_1:
                if d.keys() == dir_list.keys():
                    for element in d.values():
                        for count, name in enumerate(element):
                            if name == '':
                                name_double = list(n for n in dir_list.values())
                                for name_replace in name_double:
                                    element[count] += name_replace[count]
    for d in dir_1:
        for d2 in d.values():
            ddd = list(d.keys())
            for d5 in ddd:
                d6 = d5.split(',') + d2
            dir_2.append(d6)
    with open(file, "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for item in dir_2:
            datawriter.writerows([item])


info_correct()
phone_correct()
write(second_text)
no_double('phonebook.csv')
























