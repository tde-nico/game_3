from scripts.entity import Entity
from scripts.standard_functions import read_file


grounds = []


def generate_ground(screen, ground):
    datas = ground.split(' ')
    grounds.append(Entity(
        screen = screen,
        x = float(datas[0]),
        y = float(datas[1]),
        width = float(datas[2]),
        height = float(datas[3]),
        color = (int(datas[4]), int(datas[5]), int(datas[6]))
        ))


def generate_ground_from_file(screen, map_file):
    ground_datas = read_file('maps\\' + map_file)
    for ground in ground_datas.strip('\n').split('\n'):
        generate_ground(screen, ground)
    return grounds, ground_datas


def generate_ground_from_data(map_data):
    for ground in map_data:
        generate_ground(screen, ground)
    return grounds


def list_maps():
    import os
    maps = []
    for map_ in os.listdir('maps'):
        maps.append(map_)
    return maps




