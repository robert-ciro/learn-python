fp = open("sample.txt")

# print(fp.read())  # hello world!

for line in fp:
    print(line)

fp.close()

fp = open("sample.txt", "w")
fp.write("Bye World!")
fp.close()
