def main():
    old_file = open('monsters_old.json', 'rt', encoding='utf8')
    new_file = open('monsters.json', 'wt', encoding='utf8')

    for line in old_file:
        # if line.__contains__('monster') & line.__contains__(':'):
        #     new_line = '    {\n'
        if line.__contains__('ability'):
            new_line = line.replace('ability', 'agility')
        else:
            new_line = line
        new_file.write(new_line)

    old_file.close()
    new_file.close()


if __name__ == '__main__':
    main()
