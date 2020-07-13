phrase = "Don't panic!"
target = 'on tap'
plist = list(phrase)

print(phrase)
print(plist)

shorter = plist[1:8]

shorter.remove("'")
shorter.append(shorter.pop(4))
shorter.insert(2, shorter.pop(3))
new_phrase = ''.join(shorter)

print(plist)
print(new_phrase)