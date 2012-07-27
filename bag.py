
#@outputSchema("y:bag{t:tuple(ip:chararray,time_in_seconds:int)}")
@outputSchema("y:bag{t:tuple(output:chararray)}")
def login_logout_sequence(records):
  date_time_uriStem_ip_list = []
  for record in records:
    year,month,day      = record[0].split('-')
    hour,minute,seconds = record[1].split(':')

    seconds = (int(year)*31557600) + (int(month)*2592000) + (int(day)*86400) + (int(hour)*3600) + (int(minute)*60) + int(seconds)
    #sorted_ip_seconds.append(seconds)
    date_time_uriStem_ip = [record[3], record[2], record[0], record[1], seconds]
    date_time_uriStem_ip_list.append(date_time_uriStem_ip)
#  return date_time_uriStem_ip

#  previous_login      = False
#  login_logout_output = ""
  login_logout_list   = []
  for date, time, uri_stem, ip, seconds in sorted(date_time_uriStem_ip_list, key=lambda date_time_uriStem_ip: date_time_uriStem_ip[4], reverse=False):
    login_logout_list.append((date + " " + time + " " + uri_stem + " " + ip))
#    if previous_login:
#      if item[2] == '/Login':
#        login_logout_output = item[3] + "\t" + item[0] + " " + item[1]
#        previous_login      =  True
#      else:
#        login_logout_output = login_logout_output + "\t" + item[0] + " " + item[1]
#        login_logout_list.append((login_logout_output))
#    else:
#      if item[2] == '/Login':
#        login_logout_output = item[3] + "\t" + "-"
#        previous_login      = True
#      else:
#        login_logout_output = item[3] + "\t" + "-"
#        login_logout_list.append((login_logout_output))
#        previous_login      = False

  return login_logout_list
