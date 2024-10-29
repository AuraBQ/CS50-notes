# Code replaces the emoticons ':)' and ':(' in any message into their emoji counterparts.
text = input("Include ':)' or ':(' in a message. ").replace(":)", "\U0001F642").replace(":(", "\U0001F641")
print(text)
