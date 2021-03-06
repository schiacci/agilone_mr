REGISTER 'bag.py' USING org.apache.pig.scripting.jython.JythonScriptEngine AS bag;

logs                = LOAD '/user/ben/u_ex120718 {$input}.log' USING PigStorage(' ') AS (date:chararray, time:chararray, s_ip:chararray, method:chararray, uri_stem:chararray, uri_query:chararray, port:chararray, username:chararray, c_ip:chararray, user_agent:chararray, status:chararray, substatus:chararray, win32Status:chararray, time_taken:chararray);

logs                = FILTER logs BY (uri_stem == '/Login') OR (uri_stem == '/Logout');

field_specific_logs = FOREACH logs GENERATE date, time, uri_stem, c_ip;

cIp_logs            = GROUP field_specific_logs BY c_ip;

ip_loginDate_loginTime_logoutDate_logoutTime = FOREACH cIp_logs GENERATE FLATTEN(bag.login_logout_sequence(field_specific_logs));

DESCRIBE ip_loginDate_loginTime_logoutDate_logoutTime;
DUMP     ip_loginDate_loginTime_logoutDate_logoutTime;
