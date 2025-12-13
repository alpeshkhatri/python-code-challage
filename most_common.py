from collections import Counter

data = ""
print("enter data (exit to exit) : ")
while (line := input()) != "exit" :
    data += line + "\n"

print(data)

data = data.replace('/','-').strip().splitlines()

# print(data)

for idx in range(0,6) :
    col = list(map(lambda x: x.split('-')[idx], data))
    print(Counter(col).most_common(1))

