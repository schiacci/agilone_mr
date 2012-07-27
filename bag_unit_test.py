#!/usr/bin/python

import bag
from sets import Set


def print_test(records, output_set):
  for record in bag.login_logout_sequence(records):
    record_string = record[0] + ' ' + record[1] + ' ' + record[2] + ' ' + record[3]
    if len(record) == 5:
      record_string = record_string + ' ' + record[4]
    record_string = record_string.strip()
    if record_string in output_set:
      print record_string, 'record FOUND in output_set'
    else:
      print record_string, 'record NOT FOUND in output_set'

#==============================================================================================
# Main code below
#==============================================================================================

output_set = Set(["192.168.1.42 2012-07-18 17:56:17 -","192.168.1.42 2012-07-18 17:59:39 -","192.168.1.42 2012-07-18 17:59:39 2012-07-18 17:59:39","71.168.72.180 2012-07-18 18:18:09 2012-07-18 18:25:50","74.125.224.40 2012-07-18 18:04:10 2012-07-18 18:05:07","74.125.224.40 - 2012-07-18 18:05:13","74.125.224.36 2012-07-18 17:49:18 -","74.125.224.101 2012-07-18 18:09:59 -"])

records = [['2012-07-18','17:56:17','/Login','192.168.1.42'],['2012-07-18','17:59:39','/Login','192.168.1.42'],['2012-07-18','17:59:39','/Login','192.168.1.42'],['2012-07-18','17:59:39','/Logout','192.168.1.42']]
print_test(records, output_set)

records = [['2012-07-18','18:18:09','/Login','71.168.72.180'],['2012-07-18','18:25:50','/Logout','71.168.72.180']]
print_test(records, output_set)

records = [['2012-07-18','17:49:18','/Login','74.125.224.36']]
print_test(records, output_set)

records = [['2012-07-18','18:04:10','/Login','74.125.224.40'],['2012-07-18','18:05:07','/Logout','74.125.224.40'],['2012-07-18','18:05:13','/Logout','74.125.224.40']]
print_test(records, output_set)

records = [['2012-07-18','18:09:59','/Login','74.125.224.101']]
print_test(records, output_set)

#Tests not in the working input set
records = [['2012-07-18','18:09:1','/Login','74.125.224.101'],['2012-07-18','18:09:1','/Login','74.125.224.101'],['2012-07-18','18:09:1','/Login','74.125.224.101'],['2012-07-18','18:09:1','/Login','74.125.224.101']]
print_test(records, output_set)

records = [['2012-01-18','18:25:50','/Logout','71.168.72.180'],['2012-01-18','18:25:49','/Logout','71.168.72.180'],['2012-01-18','18:25:48','/Logout','71.168.72.180'],['2012-01-18','18:25:48','/Logout','71.168.72.180']]
print_test(records, output_set)

records = [['2012-01-18','18:25:50','/Login','171.168.72.180'],['2012-01-18','18:25:49','/Logout','171.168.72.180']]
print_test(records, output_set)


records = [['2012-01-18','18:25:50','/Login','171.168.72.180'],['2012-01-18','18:25:51','/Logout','171.168.72.180']]
print_test(records, output_set)
