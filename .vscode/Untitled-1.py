text = "This is the text i want to affect"
italic = "\033[3m"
bold = "\033[1m"
color = "\033[35m"
reset = "\033[0m"
print (italic + bold + text + color + reset)
print (text)