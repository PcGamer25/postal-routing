class Package:

    # Constructor for a package
    def __init__(self, id, address, city, state, zip, deadline, weight, special, status="AT THE HUB"):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status

    # Sets the package status to delivered with a timestamp
    def set_delivered(self, time):
        self.status = "DELIVERED AT " + time.strftime('%I:%M %p')

    # Prints the current status of a package
    def print_status(self):
        address = self.address + ", " + self.city + ", " + self.state + " " + self.zip
        status = "ID: {:<10}{:30}{:70}{:15}{} kg".format(self.id, self.status, address, self.deadline, self.weight)
        if 'DELIVERED' in status:
            print('\033[32m' + status)
        elif 'EN ROUTE' in status:
            print('\033[33m' + status)
        else:
            print('\033[31m' + status)
