word = input()
password = ''

for character in range(0, len(word)):
    if word[character] == 'i':
        password = password +  '!'
    elif word[character] == 'a':
        password = password +  '@'
    elif word[character] == 'm':
        password = password +  'M'      
    elif word[character] == 'B':
        password = password +  '8' 
    elif word[character] == 'o':
        password = password +  '.' 
    else:
        password = password + word[character]


print(password + 'q*s')
