import re

from input_reader import puzzle_input


def part1():
    nth_sec = 2503
    result = []
    for i in puzzle_input("actual", '13'):
        speed, time1, time2 = re.findall(r'\d+', i)
        speed = int(speed)
        time1 = int(time1)
        time2 = int(time2)
        # print(speed, time1, time2)
        extra_time = nth_sec % (time1 + time2)
        if extra_time // time1 > 1:
            x = speed * time1
        else:
            x = speed * extra_time
        # print("Extra time:", extra_time, "Extra distance:", x)
        result.append((nth_sec//(time1 + time2) * speed * time1) + x)
    # print(result)
    print(max(result))


def part2():
    data = {}
    for i in puzzle_input("actual", '13'):
        speed, time1, time2 = re.findall(r'\d+', i)
        data[i.split(' ')[0]] = {"speed": int(speed), "time1": int(time1), "time2": int(time2), "distance": 0, "points": 0}
    for i in range(1, 2504):
        # print(i)
        for reindeer in data.keys():
            if ((i % (data[reindeer]["time1"] + data[reindeer]["time2"])) != 0 and
                    (i % (data[reindeer]["time1"] + data[reindeer]["time2"])) <= data[reindeer]["time1"]):
                data[reindeer]["distance"] += data[reindeer]["speed"]
        temp_max = 0
        point_getter = ''
        for reindeer, items in data.items():
            if temp_max < items['distance']:
                temp_max = items['distance']
                point_getter = reindeer
        data[point_getter]["points"] += 1
        # print(point_getter)
        # print(data)

    print(max(int(d['points']) for d in data.values()))


part1()
part2()