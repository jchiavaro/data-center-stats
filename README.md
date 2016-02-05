# data-center-stats
===================

### Execute the app
Clone the git repository: https://github.com/jchiavaro/data-center-stats.git
* Go to the app directory:
- cd app

* A Python executable script is provided: from the app directory,
execute the data_center.py script:
- ./data_center.py customerID hotID datacentreID [options]
Check the help for more information about the program arguments:
- ./data_center.py -h or ./data_center.py --help

## Example
- ./data_center.py 8 2 0 -f hosts.txt -i instances.txt -s stats.txt
It will run the program using the "hosts.txt" and "instances.txt" files as inputs
and creates the "stats.txt" file with the respective statistics for customer 8,
host 2 and datacentre 0 (customer, host, and datacentre are mandatory args).
If no optional args regarding to the files are specified, the program will try to run
with the default provided text files: "HostState.txt" and "InstanceState.txt" as inputs,
and it will generate an output file "statistics.txt"

## Logging
The program generates the datacentre.log containing important logging info for debugging purposes.
By default logs at the DEGUG level.

##Running unit tests:
For running all the unit tests, go to the app directory: cd app
and run the following command:
- python -m unittest discover -p '*_test.py'

It will run all the unit tests inside the "test" directory.

## Help
usage: data_center.py [-h] [-f HOSTSFILE] [-i INSTANCESFILE] [-s SFILE]
                      customer host datacentre

Calculate statistics for hosts and customers

positional arguments:
  customer              The customerID for statistics - i.e: 3
  host                  The hostID for statistics - i.e: 8
  datacentre            The datacentreID for statistics - i.e: 1

optional arguments:
  -h, --help            show this help message and exit
  -f HOSTSFILE, --hostsfile HOSTSFILE
                        Read data from the hosts file: i.e: hosts.txt
  -i INSTANCESFILE, --instancesfile INSTANCESFILE
                        Read data from the instances file - i.e: instances.txt
  -s SFILE, --sfile SFILE
                        Write statistics data to the specified file - i.e:
                        statistics.txt
