HadoopVersion: 0.20.3-dev	
PigVersion:    0.10.0


Example run:
hadoop dfs -put logs/u_ex120718\ 1.log u_ex120718\ 1.log;hadoop dfs -put logs/u_ex120718\ 2.log u_ex120718\ 2.log;hadoop dfs -put logs/u_ex120718\ 3.log u_ex120718\ 3.log;hadoop dfs -put logs/u_ex120718\ 4.log u_ex120718\ 4.log;pig --param input=1,2,3,4 log_processor.pig

parameters input: '1,2,3,4' is the X in u_ex120718\ X.log.  I was having problems with spaces.  Typically, I try to replace spaces with underscores during normal data processing.

unit test of mapper:
python bag_unit_test.py
