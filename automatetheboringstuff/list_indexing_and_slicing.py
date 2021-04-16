spam = ['cat', 'bat', 'rat', 'elephat', 'dog', 'car', 1, 5]

spam_1 = spam[0:3]


spam_2 = spam[3:]

# do not from beginning up to but not including index 3
spam_3 = spam[:3]

joined_spam = spam_1 + spam_2
print(joined_spam)