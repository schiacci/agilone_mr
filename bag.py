
def login_logout_sequence(records):
  date_time_uriStem_ip_seconds_list = []
  # Read each bag item and append a time in estimated seconds
  seconds_dateTimeUriStemIpSeconds_map = {}
  found_duplicate                      = False
  for record in records:
    year,month,day      = record[0].split('-')
    hour,minute,seconds = record[1].split(':')

    seconds = (int(year)*31557600) + (int(month)*2592000) + (int(day)*86400) + (int(hour)*3600) + (int(minute)*60) + int(seconds)
    date_time_uriStem_ip_seconds = [record[0], record[1], record[2], record[3], seconds]
    date_time_uriStem_ip_seconds_list.append(date_time_uriStem_ip_seconds)

    if seconds in seconds_dateTimeUriStemIpSeconds_map:
      found_duplicate = True
    if seconds not in seconds_dateTimeUriStemIpSeconds_map:
      seconds_dateTimeUriStemIpSeconds_map[seconds] = []
    seconds_dateTimeUriStemIpSeconds_map[seconds].append(date_time_uriStem_ip_seconds)

  #=================================================================================================
  # Handle duplicate order login first then logout
  #=================================================================================================
  if found_duplicate:
    reordered_date_time_uriStem_ip_seconds_list = []
    for seconds, date_time_uriStem_ip_seconds_list in seconds_dateTimeUriStemIpSeconds_map.iteritems():
      if len(date_time_uriStem_ip_seconds_list) == 1:
        reordered_date_time_uriStem_ip_seconds_list.append(date_time_uriStem_ip_seconds_list[0])
      else:
        temp_date_time_uriStem_ip_seconds_list = date_time_uriStem_ip_seconds_list
        cont = True
        while len(temp_date_time_uriStem_ip_seconds_list) > 0:
          appended_login = False
          for possible_login in date_time_uriStem_ip_seconds_list:
            if possible_login[2] == '/Login' and possible_login in temp_date_time_uriStem_ip_seconds_list:
              temp_date_time_uriStem_ip_seconds_list.remove(possible_login)
              reordered_date_time_uriStem_ip_seconds_list.append(possible_login)
              appended_login = True
              break
          if appended_login == False:
            break
           
          appended_logout = False
          for possible_logout in date_time_uriStem_ip_seconds_list:
            if possible_logout[2] == '/Logout' and possible_logout in temp_date_time_uriStem_ip_seconds_list:
              temp_date_time_uriStem_ip_seconds_list.remove(possible_logout)
              reordered_date_time_uriStem_ip_seconds_list.append(possible_logout)
              appended_logout = True
              break
          if appended_logout == False:
            break
        for date_time_uriStem_ip_seconds in temp_date_time_uriStem_ip_seconds_list:
          reordered_date_time_uriStem_ip_seconds_list.append(date_time_uriStem_ip_seconds)
    date_time_uriStem_ip_seconds_list = reordered_date_time_uriStem_ip_seconds_list
  #=================================================================================================

  #=================================================================================================
  # loop through each item in order in seconds (stable sort for duplicates seconds)
  #=================================================================================================
  previous_login       = False
  ip_login_logout_list = []
  current_ip           = None
  login_date           = None
  login_time           = None
  logout_date          = None
  logout_time          = None  
  for date_time_uriStem_ip_seconds in sorted(date_time_uriStem_ip_seconds_list, key=lambda date_time_uriStem_ip: date_time_uriStem_ip[4], reverse=False):
    if date_time_uriStem_ip_seconds[2] == '/Login':
      # Previous was login, no logout called
      if previous_login and login_date and login_time:
        ip_login_logout_list.append((current_ip, login_date, login_time, '-'))
        current_ip           = None
        login_date           = None
        login_time           = None
        logout_date          = None
        logout_time          = None

      current_ip = date_time_uriStem_ip_seconds[3]
      login_date = date_time_uriStem_ip_seconds[0]
      login_time = date_time_uriStem_ip_seconds[1]

      previous_login = True

    elif date_time_uriStem_ip_seconds[2] == '/Logout':
      current_ip  = date_time_uriStem_ip_seconds[3]
      logout_date = date_time_uriStem_ip_seconds[0]
      logout_time = date_time_uriStem_ip_seconds[1]
      if previous_login:
        ip_login_logout_list.append((current_ip, login_date, login_time, logout_date, logout_time))
      else:
        # no prior login
        ip_login_logout_list.append((current_ip, '-', logout_date, logout_time))
      current_ip           = None
      login_date           = None
      login_time           = None
      logout_date          = None
      logout_time          = None  
        
      previous_login = False

  # login found without a last login or logout
  if login_date and login_time:
    ip_login_logout_list.append((current_ip, login_date, login_time, '-'))

  return ip_login_logout_list

