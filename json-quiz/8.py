import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']


s_sum = 0
for b in books:
    if b['publisher'] == 'Scribner':
        s_sum += 1

print("A.", s_sum)

d_sum = 0
for b in books:
    if "detective" in b['description'].lower():
        d_sum += 1

print("B.", d_sum)

from operator import itemgetter
y = sorted(books, key = itemgetter('weeks_on_list'), reverse = True)
x = y[0]
print('C.', '%s|%s' % (x['title'], x['weeks_on_list']))

y = sorted(books, key = itemgetter('rank_last_week'), reverse = True)
x = y[0]
# alternatively:
# x = max(accounts, key = itemgetter('followers_count'))
print('D.', '%s|%s|%s' % (x['title'], x['rank'], x['rank_last_week']))

new = []
for b in books:
    if b['rank_last_week'] == 0:
        new.append(b)
print('E.', len(new))

matrix = sorted(new, key = itemgetter('rank'))
x = matrix[0]
print("F.", '%s|%s' % (x['title'], x['rank']))


################## 
# Task G.
# define a helper function
def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)

################## 
# Task I
# (assuming books_ranked_last_week and calc_rank_change() have 
#    been defined as above)
changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)

changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for m in changes if m < 0]
w = sum(x)
print("J.", '%s|%s' % (len(x), w))

###################
# Task K
print('K.', max([len(b['title']) for b in books]))

x = round(sum([len(b['title']) for b in books]) / len(books))
print('L.', x)