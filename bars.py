import json
import math


def get_distance(coord_A, coord_B):
    return math.sqrt((coord_A[0] - coord_B[0]) * (coord_A[0] - coord_B[0]) +
                     (coord_A[1] - coord_B[1])*(coord_A[1] - coord_B[1]))


def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return(data)


def get_biggest_bar(sorted_data):
    return sorted_data[0]['Cells']['Name']


def get_smallest_bar(sorted_data):
    return sorted_data[-1]['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    coord_bar = data[0]['Cells']['geoData']['coordinates']
    bar_norm = get_distance(coord_bar, [longitude, latitude])
    closest_bar = {'name': data[0]['Cells']['Name'], 'norm': bar_norm}
    for bar in data[1:]:
        coord_bar = bar['Cells']['geoData']['coordinates']
        bar_norm = get_distance(coord_bar, [longitude, latitude])
        if closest_bar['norm'] > bar_norm:
            closest_bar = {'name': bar['Cells']['Name'], 'norm': bar_norm}
    return closest_bar['name']


def get_sorted_data():
    data = load_data('source/bar.json')
    data.sort(key=lambda x: x['Cells']['SeatsCount'], reverse=True)
    return data


if __name__ == '__main__':
    sorted_data = get_sorted_data()
    print('The biggest bar is %s' % get_biggest_bar(sorted_data))
    print('The smallest bar is %s' % get_smallest_bar(sorted_data))
    longitude = float(input("Enter coordinates (long): "))
    latitude = float(input("Enter coordinates (lati): "))
    print('The closest bar is %s' % get_closest_bar(sorted_data,
                                                    longitude,
                                                    latitude))
