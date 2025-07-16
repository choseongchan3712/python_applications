with open('new_file.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world!\n")
    f.write("my name is otter\n")

with open('new_file.txt', 'a', encoding='utf-8') as f:
    f.write("Hello world!\n")
    f.write("my name is otter\n")