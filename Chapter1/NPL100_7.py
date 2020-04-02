def template_string(x, y, z):
    return "{hour}時の{target}は{value}".format(hour = x, target = y, value = z)

print(template_string(12, "気温", 22.4))