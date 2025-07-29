# file1 = open('files/016-a.txt', 'r')
# file1extracted = file1.readlines()
# for items in file1extracted:
#     print(items)
#     file1.close()
#
# file2 = open('files/016-b.txt', 'r')
# file2extracted = file2.readlines()
# for items in file2extracted:
#     print(items)
#     file2.close()
#
# file3 = open('files/016-c.txt', 'r')
# file3extracted = file3.readlines()
# for items in file3extracted:
#     print(items)
#     file3.close()

files = ["files/016-a.txt", "files/016-b.txt", "files/016-c.txt"]

for file in files:
    with open(file, 'r') as f:
        for line in f:
            print(line)
