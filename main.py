from stations import *

#give list of all MRT stations
def show_list():
    for station in stations.keys():
        print(station)

#finding the start and end points
def input_start_and_end():
    start = input("What station are you originating from? ")
    while start not in stations.keys():
        start = input("Please input a valid station: ")
    end = input("Where is your destination? ")
    while end not in stations.keys():
        end = input("Please input a valid station: ")
    return start, end

#breadth first search
def bfs(graph, start, end):
    path = [start]
    station_and_path = [start, path]
    queue = [station_and_path]
    visited_stations = set()

    while queue:
        current_station, path = queue.pop(0)
        visited_stations.add(current_station)

        for station in stations[current_station]:
            if station not in visited_stations:
                if station == end:
                    return path + [station]
                else:
                    queue.append([station, path + [station]])

def main():
    show_list()
    start, end = input_start_and_end()
    station_route = bfs(stations, start, end)
    print(f'Your shortest path to {end} is:')
    for i in range(len(station_route)):
        print('{}. {}'.format(i+1, station_route[i]))

main()
