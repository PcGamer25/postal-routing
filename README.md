# Postal Routing Program
postal-routing is a program that simulates efficient and on time delivery of mail packages for the Western Governors University Parcel Service.

A total of 40 packages must be delivered. Three mail trucks and two drivers are available to make the deliveries. A map of downtown Salt Lake City and distances between delivery locations are provided in a spreadsheet.
## Assumptions and Criteria
- All 40 packages must be delivered on time
- A package may have specific delivery deadlines
- The combined total distance traveled by the mail trucks must be under 140 miles
- Each truck travels at an average speed of 18 miles per hour (accounting for delivery and loading times)
- Each truck can carry a maximum of 16 packages
- There are no collisions of trucks
- The drivers must stay with the same truck as long as it is in service
- Drivers cannot leave the hub earlier than 8:00 a.m.
- Drivers can return to the hub for packages if necessary
- Unknown to the program, the address for one package is incorrect and will be corrected at 10:20 a.m.
## Requirements for the Program
- As an exercise, a custom hash table must be created to store and retrieve the package data
- The status of each truck’s packages can be displayed at any point in time
- The status and delivery timestamps for each package can be displayed at any point in time
## Solution
A heuristic using the nearest neighbor algorithm is implemented in the solution. The algorithm sorts the addresses of the packages and quickly produces sufficiently efficient routes for the three trucks. All packages are delivered on time with a total truck mileage of 103.9 miles, well under the 140-mile constraint.

To further learn about data structures, a custom hash table is implemented in the `hashtable.py` module. The hash table handles the insertion, storage, and retrieval of packages.
## Example Program Output
### Status report at 9:00 a.m.
<img width="828" alt="postal9" src="https://github.com/PcGamer25/postal-routing/assets/24723469/f404d33d-6e58-4cd1-aeca-60593dbcdd10">

### Status report at 12:00 p.m.
<img width="828" alt="postal12" src="https://github.com/PcGamer25/postal-routing/assets/24723469/b538fe9c-7285-4225-9c9c-0f101ce1b3a3">
