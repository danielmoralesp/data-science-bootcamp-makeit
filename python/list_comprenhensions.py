words = ["@coolguy95", "#nofilter", "@books", "reply", "timestamp", "@match", "follow", "#updog"]

usernames = []

for word in words:
    if word[0] == '@':
        usernames.append(word)

print(usernames)

usernames = [word for word in words if word[0] == '@']
print(usernames)

usernames = ['@coolguy95', '@books', '@match']


messages = [user + " porfavor sigueme en facebook" for user in usernames]
print(messages)

my_upvotes = [192, 75, 95, 78, 5, 45]
updated_votes = [vote_value + 100 for vote_value in my_upvotes]


celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [frh * 9/5 + 32 for frh in celsius]
print(fahrenheit)
