import re
import pdb
# # s="123 ?? word"
# word_re = re.compile(r'\w+')
# # print(word_re.search(s))
# index = {}
# with open('input.txt', encoding='utf-8') as fp:
#     pdb.set_trace()
#     # 1 表示标号从1开始
#     for line_no, line in enumerate(fp,1):
#         for match in word_re.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
pdb.set_trace()
regEx=re.compile('\\W+')
listOfTokens=regEx.split(mySent)
print(listOfTokens)
