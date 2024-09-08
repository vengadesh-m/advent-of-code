from input_reader import puzzle_input


def part1():
    search_list = """children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1 """
    data = {}
    search_list = search_list.split('\n')
    # print(search_list)
    new_list = {}
    for i in search_list:
        a, b = i.split(':')
        new_list[a.strip()] = b.strip()

    print(new_list)
    for i in puzzle_input("sample", 15):
        _, aunt, a1, v1, a2, v2, a3, v3 = i.split(' ')
        data[aunt.strip(':')] = {a1.strip(':'): v1.strip(','), a2.strip(':'): v2.strip(','), a3.strip(':'): v3.strip('\n')}
    print(data)

    for aunt_num, items in data.items():
        counter = 0
        for item, value in items.items():
            if new_list.get(item) == value:
                counter += 1
        if counter == 3:
            print(aunt_num)
            break


def part2():
    search_list = """children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1 """
    data = {}
    search_list = search_list.split('\n')
    # print(search_list)
    new_list = {}
    for i in search_list:
        a, b = i.split(':')
        new_list[a.strip()] = int(b.strip())

    print(new_list)
    for i in puzzle_input("sample", 15):
        _, aunt, a1, v1, a2, v2, a3, v3 = i.split(' ')
        data[aunt.strip(':')] = {a1.strip(':'): int(v1.strip(',')), a2.strip(':'): int(v2.strip(',')), a3.strip(':'): int(v3.strip('\n'))}
    print(data)

    for aunt_num, items in data.items():
        counter = 0
        if aunt_num == '1':
            print()
        for item, value in items.items():
            if item in ('cats', 'trees') and value > new_list.get(item):
                counter += 1
            if item in ('pomeranians', 'goldfish') and value < new_list.get(item):
                counter += 1
            if item not in ('cats', 'trees', 'pomeranians', 'goldfish') and new_list.get(item) == value:
                counter += 1
        if counter == 3:
            print(aunt_num)
            break


# part1()
part2()