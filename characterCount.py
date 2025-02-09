import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count[character] = count.get(character, 0) + 1

pprint.pprint(count)