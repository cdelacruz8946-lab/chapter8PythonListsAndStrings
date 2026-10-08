fhand = open('mbox-short.txt', 'r')
fhand = fhand.read()
arise = fhand
arise = arise.split('Sat Jan 5 09:14:16 2008')
words = arise
words.append('louis@media.berkeley.edu zqian@umich.edu rjlowe@iupui.edu zqian@umich.edu rjlowe@iupui.edu cwen@iupui.edu')

print(words)
print(len(words))