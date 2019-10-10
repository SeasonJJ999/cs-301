total = 0
count = 0

while True:
    val = input('Enter a percent, please [q for exit]:')
    if val == 'q':
        break
    val = int(val)
    if not (0<=val<=100):
        print('Yikes! Not in the range!')
        continue
    else:
        print(val,'%')
