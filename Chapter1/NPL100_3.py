import re
string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sp_string = re.findall('[^,. ]+', string)
num_string = list(map(lambda s: len(s), sp_string))
print(num_string)