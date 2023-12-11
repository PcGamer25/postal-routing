import csv
import datetime

from hashtable import MyHashTable
from package import Package
from truck import Truck


# Parses the package and distance CSV files for data
# Inserts packages into the custom hash table
def parse():
    with open('WGUPS Package File CSV.csv', 'r') as package_csv:
        package_reader = csv.reader(package_csv)

        for line in package_reader:
            packages.update(int(line[0]),
                            Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7]))

    with open('WGUPS Distance Table CSV.csv', 'r') as distance_csv:
        distance_reader = csv.reader(distance_csv)

        for line in distance_reader:
            if len(addresses) < 27:
                addresses.append(line[1])
            else:
                distances.append(line)


# Returns the distance in miles between two addresses
def distance(address1, address2):
    index1 = addresses.index(address1)
    index2 = addresses.index(address2)

    if index1 < index2:
        return float(distances[index2][index1])
    return float(distances[index1][index2])


# Returns a sorted list of addresses using the nearest neighbor algorithm
def nearest_neighbor(unsorted):
    sorted = []

    unsorted.insert(0, '4001 South 700 East')
    curr_address = unsorted[0]
    next_address = unsorted[1]

    while True:
        smallest_distance = distance(curr_address, next_address)
        for address in unsorted:
            this_distance = distance(curr_address, address)
            if 0 < this_distance < smallest_distance:
                smallest_distance = this_distance
                next_address = address

        sorted.append(next_address)
        unsorted.remove(curr_address)
        curr_address = next_address
        next_address = unsorted[0]
        if next_address == curr_address:
            if len(unsorted) == 1:
                unsorted.remove(curr_address)
                break
            next_address = unsorted[1]

    return sorted


# Returns a list of unique addresses from a group of packages
def get_unique_addresses(packages):
    unique_addresses = []
    for package in packages:
        if package.address not in unique_addresses:
            unique_addresses.append(package.address)

    return unique_addresses


# Delivers packages until a requested time constraint
def truck_away(truck, requested_time):
    if requested_time >= truck.time:
        for package in truck.packages:
            package.status = "EN ROUTE"

        for destination in truck.route:
            truck.time += datetime.timedelta(hours=distance(truck.location, destination) / truck.speed)
            if requested_time >= truck.time:
                truck.mileage += distance(truck.location, destination)
                for package in truck.packages:
                    if package.address == destination:
                        package.set_delivered(truck.time)

            truck.location = destination


# Prints the status of all packages on a truck
def print_status(truck):
    print("\n\033[0mTruck", truck.id)
    print("Miles traveled:", round(truck.mileage, 2))
    print("{:14}{:30}{:70}{:15}{}".format('Package', 'Status', 'Address', 'Deadline', 'Weight'))
    truck.packages.sort(key=lambda package: package.status)
    for package in truck.packages:
        package.print_status()


# Runs the user interface for the program
def ui():
    print("\n===================================================")
    print("Western Governors University Parcel Service Tracker")
    print("===================================================\n")
    print("Please enter a package ID to view tracking information. Leave blank for all packages.")
    requested_package_id = input("Package ID: ")
    try:
        requested_package_id = int(requested_package_id)
        print("For package " + str(requested_package_id) + ", ", end="")
    except:
        requested_package_id = None
        print("For all packages, ", end="")
    print("please enter a point in time to view tracking information (format 24:00). Leave blank for end of day.")
    requested_time_input = input("Time: ")
    requested_time = datetime.datetime.strptime('23:59:59', '%H:%M:%S')
    try:
        requested_time = datetime.datetime.strptime(requested_time_input, '%H:%M')
        print()
    except:
        print("Showing tracking information for end of day.\n")

    truck_away(truck1, requested_time)
    truck_away(truck2, requested_time)
    truck_away(truck3, requested_time)

    if requested_package_id is not None:
        all_packages = truck1.packages + truck2.packages + truck3.packages
        for package in all_packages:
            if package.id == requested_package_id:
                print("{:14}{:30}{:70}{:15}{}".format('Package', 'Status', 'Address', 'Deadline', 'Weight'))
                package.print_status()
                break
        else:
            print("\033[31mPackage not found")

    if requested_package_id is None:
        print("Total miles traveled by all trucks:", round(truck1.mileage + truck2.mileage + truck3.mileage, 2))

        print_status(truck1)
        print_status(truck2)
        print_status(truck3)


packages = MyHashTable()
addresses = []
distances = []
parse()

# Separating the packages into batches for each truck
batch1 = [packages.get(15),
          packages.get(1),
          packages.get(13),
          packages.get(14),
          packages.get(16),
          packages.get(20),
          packages.get(29),
          packages.get(30),
          packages.get(31),
          packages.get(34),
          packages.get(37),
          packages.get(40),
          packages.get(19),
          packages.get(2),
          packages.get(4),
          packages.get(5)]
batch2 = [packages.get(3),
          packages.get(18),
          packages.get(36),
          packages.get(38),
          packages.get(6),
          packages.get(25),
          packages.get(28),
          packages.get(32),
          packages.get(7),
          packages.get(8),
          packages.get(10),
          packages.get(11),
          packages.get(12),
          packages.get(17),
          packages.get(22),
          packages.get(23)]
batch3 = [packages.get(9),
          packages.get(21),
          packages.get(24),
          packages.get(26),
          packages.get(27),
          packages.get(33),
          packages.get(35),
          packages.get(39)]

# Correcting package #9 address to be shipped out at 10:20 AM after correction
packages.get(9).address = '410 S State St'
packages.get(9).city = 'Salt Lake City'
packages.get(9).state = 'UT'
packages.get(9).zip = '84111'

# Creating three trucks
truck1 = Truck(datetime.datetime.strptime("8", '%H'))
truck2 = Truck(datetime.datetime.strptime("9:05", '%H:%M'))
truck3 = Truck(datetime.datetime.strptime("10:20", '%H:%M'))

# Loading the trucks
truck1.load(batch1)
truck1.route = nearest_neighbor(get_unique_addresses(batch1))
truck1.route.append('4001 South 700 East')

truck2.load(batch2)
truck2.route = nearest_neighbor(get_unique_addresses(batch2))
truck2.route.append('4001 South 700 East')

truck3.load(batch3)
truck3.route = nearest_neighbor(get_unique_addresses(batch3))
truck2.route.append('4001 South 700 East')

# Starting the user interface
ui()
