import re

equation = input()

n1, n2, n3 = map(int, re.split('[x=]', equation))

n3 += n2*-1
n3 /= n1

print("%.2f" %n3)

