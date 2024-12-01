from input_reader import puzzle_input

results = {}
operator_mapping = {'AND': '&', 'OR': '|', 'NOT': '', 'LSHIFT': '<<', 'RSHIFT': '>>'}


def resolve_expressions(exp):
    exp = exp.split(' ')
    if len(exp) == 1 and exp[0].isdigit():
        return int(exp[0])
    if len(exp) == 3:
        f, s, t = exp
        if (rf := results.get(f) and type(results.get(f)) == str and results.get(f).isdigit()) and (rt := results.get(t) and type(results.get(t)) == str and results.get(t).isdigit()):
            return eval(f'{rf} {operator_mapping[s]} {rt}')
        if (rf := results.get(f) and type(results.get(f)) == str and results.get(f).isdigit()) and t.isdigit():
            return eval(f'{rf} {operator_mapping[s]} {int(t)}')
    if len(exp) == 2 and exp[1].isdigit():
        return 65535 - int(results.get(exp[1]))


def part1_old():
    for i in puzzle_input():
        out = i.split(' -> ')
        results[out[-1].strip('\n')] = out[0]
    for k, v in results.items():
        results[k] = resolve_expressions(v)
    print(results)


def recursive_find(v):
    for i in puzzle_input():
        if f' -> {v}\n' in i:
            if i.split(' -> ')[0].isdigit():
                results[v] = int(i.split(' -> ')[0])
            else:
                recursive_find(i.split(' -> ')[0])
            if len(i.split(' -> ')[0].split(' ')) == 3:
                if not results.get(i.split(' -> ')[0].split(' ')[0]):
                    recursive_find(i.split(' -> ')[0].split(' ')[0])
                if not results.get(i.split(' -> ')[0].split(' ')[2]):
                    recursive_find(i.split(' -> ')[0].split(' ')[2])


def part1():
    recursive_find('a')
    print(results)


part1()
