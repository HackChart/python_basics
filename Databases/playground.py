from blessings import Terminal

t = Terminal()

print(t.bold('This should be bold'))
print(t.black + t.on_red(' This should be red '))

print(t.bold_black_on_white('What does this look like?'))
print(t.reverse('Reversed'))
print(t.blink('Blink'))
print(t.underline('underline'))
print('H' + t.subscript('2')) # Not working
print(t.standout('standout'))
print(t.shadow('shadow'))
print(t.italic('italic'))
print(t.number_of_colors)

print('This last word should be{t.bold} bold'.format(t=t))
print(t.clear)
for i in range(t.number_of_colors + 1):
    print(f'{t.color(i)}{i}', end=', ')


