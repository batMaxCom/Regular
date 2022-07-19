from pprint import pprint
import csv
import re

#
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
text = []
for t in contacts_list:
    t = ','.join(t)
    pattern = re.compile(r"(\w+)[\s,](\w+)[\s|,]?(\w+)?,(,{1,2})?(\w+)?([,]{1,2})?(\w+[^0-9+,]*)?,(\w*|(\+7|8)([ \(]*)?(\d{3})[- \)]*(\d{3})[- \)]*(\d{2})[- \)]*(\d{2})([ \(]*)?(доб.)?( )?(\d*)?)[\,)],?([\S*\(\)]*)")
    result = pattern.sub(r"\1, \2, \3, \5, \7, \8, \19", t)
    text.append([result])





second_text = []
for t_2 in text:
    t_2 = ','.join(t_2)
    pattern_2 = re.compile(r"(\+7|8)([ \(]*)?(\d{3})[- \)]*(\d{3})[- \)]*(\d{2})[- \)]*(\d{2})([ \(]*)?(доб.)?( )?(\d*)?")
    result_2 = pattern_2.sub(r'+7(\3)\4\5\6 \8\10', t_2)
    second_text.append([result_2])


with open("phonebook.csv", "w", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  for item in second_text:
    datawriter.writerows([item])

