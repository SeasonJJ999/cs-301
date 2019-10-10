import sys
print(sys.argv)
for x in sys.argv[1:]:
    total += int(x)
print(total)
