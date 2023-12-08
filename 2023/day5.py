"Day 5 solution of AoC"
import re
import os
from collections import defaultdict

result = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day5.txt"

# Inefficient way of doing
def map_generator(max_seeds, seed_to_soil):
    seed_to_so_map = {}
    for i in seed_to_soil.strip('\n\n').split('\n'):
        soil, seed, r = i.split()
        soil = int(soil)
        seed = int(seed)
        r = int(r)
        for i in range(r):
            seed_to_so_map[seed] = soil
            seed += 1
            soil += 1
    # print(len(seed_to_so_map))
    return seed_to_so_map

def efficient_generator(data, value):
    result = value
    for i in data.strip('\n\n').split('\n'):
        source, destination, r = i.split()
        source = int(source)
        destination = int(destination)
        r = int(r)
        if destination <= int(value) < destination + r:
            result = value - destination + source
    return result


with open(file) as _file:
    lines = _file.read()
    _, seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, ligh_to_temp, temp_to_humd, humid_to_location  = re.split(
        'seeds: |seed-to-soil map:|soil-to-fertilizer map:|fertilizer-to-water map:|water-to-light map:|light-to-temperature map:|temperature-to-humidity map:|humidity-to-location map:',
          lines)
    seeds = seeds.strip('\n\n').split()
    locations = []
    for seed in seeds:
        seed = int(seed)
        soil = efficient_generator(seed_to_soil, seed)
        fert = efficient_generator(soil_to_fert, soil)
        water = efficient_generator(fert_to_water, fert)
        light = efficient_generator(water_to_light, water)
        temp = efficient_generator(ligh_to_temp, light)
        humd = efficient_generator(temp_to_humd, temp)
        location = efficient_generator(humid_to_location, humd)
        # print(seed, soil, fert, water, light, temp, humd, location)
        locations.append(location)
    print(min(locations))
    
