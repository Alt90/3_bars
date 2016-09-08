import json, math

def norm(coord_A, coord_B):
    return math.sqrt((coord_A[0]-coord_B[0])*(coord_A[0]-coord_B[0])+
        (coord_A[1]-coord_B[1])*(coord_A[1]-coord_B[1]))

def load_data(filepath):
    data = []
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return(data)


def get_biggest_bar(data):
    return data[-1]['Cells']['Name']


def get_smallest_bar(data):
    return data[0]['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    closest_bar = {'name': None, 'norm': 10000}
    for bar in data:
        coord_bar = bar['Cells']['geoData']['coordinates']
        bar_norm = norm(coord_bar, [longitude, latitude])
        if closest_bar['norm'] > bar_norm:
            closest_bar = {'name': bar['Cells']['Name'], 'norm': bar_norm}
    return closest_bar['name']

if __name__ == '__main__':
    data = load_data('source/bar.json')
    data.sort(key=lambda x: x['Cells']['SeatsCount'])
    print('The biggest bar is %s' % get_biggest_bar(data))
    print('The smallest bar is %s' % get_smallest_bar(data))
    longitude = float(input("Enter coordinates (long): "))
    latitude = float(input("Enter coordinates (lati): "))
    print('The closest bar is %s' % get_closest_bar(data, longitude, latitude))
    
    
