# elb_exercise

AWS chapter:
------------

Use any automation tool you'd like to accomplish the following task.

The following environment should be created (and preferably also deleted) with a single shell command:
 
- Create an ELB + security group to listen on incoming traffic on port 80, from anywhere.
- Create an additional security group which listens on port 8080 for requests from the ELB only.
- Deploy 2 Linux instances (choose any distro you’d like) and provision as following -
  - Install a web server (Apache, nginx, etc.)
  - Deploy a demo service that listens on port 8090 and displays the instance-id and the region name.
    You can use any framework you know, e.g. Python Flask, Ruby Sinatra, Node.js Express, etc.
  - Point the web server to the demo service port (8090) to return answers on port 8080.
  - Make sure this demo service survives an instance restart (use any tool you’d like for this purpose)
- Connect the EC2 instances to the ELB
- Bonus – check the health status of the demo service from the web server and
  return an error to the ELB when it’s down.

AWS chapter solution:
---------------------

1) in order to create automated stack:
   aws cloudformation create-stack --template-body file://templates/elb-stack.yml --stack-name name

2) in order to detele cteated stack:
   aws cloudformation delete-stack --stack-name name

NOTE: make sure that aws-cli has all needed credentials.





SQL chapter:
------------

- You are given this table – preventions (key is event_guid)

- Please provide a single query that outputs a single table as presented in the image below:
  - The most common father filenames for the ‘Ransom’ module (in the image below ‘usctrl.exe’ is the most common father filename)
  - How many preventions are there per filename (e.g., 9415 ‘Ransom’ preventions for ‘usctrl.exe’)
  - The percentage value of the number of preventions out of the total number of preventions for the ‘Ransom’ module
    (e.g., 56.56% of the ‘Ransom’ preventions were for ‘usctrl.exe’)
  - common_filepath – the most common Father_path for each Father_filename in the table (Ransom preventions). 
For example: ‘C:\Program Files\CassieUserStation\usctrl.exe’ is the most common ‘Father_path’ field for all ‘Ransom’ preventions of the ‘usctrl.exe’ Father_filename.

SQL chapter solution:
---------------------

- Created SQL Schema:

CREATE TABLE IF NOT EXISTS `prev` (
  `event` int(32) unsigned NOT NULL,
  `f_path` varchar(200),
  `f_filename` varchar(200),
  `module` varchar(200),
  PRIMARY KEY (`event`)
);
INSERT INTO `prev` (`event`,`f_path`, `f_filename`, `module`) VALUES
  ('1', '/bb/a.exe', 'a.exe', 'ransom'),
  ('2', '/aa/a.exe', 'a.exe', 'ransom'),
  ('3', '/aa/a.exe', 'a.exe', 'ransom'),
  ('4', '/aa/b.exe', 'b.exe', 'ransom'),
  ('5', '/usr/sbin/xinetd', 'xinetd', 'SocketShaell');


- SQL Query:

SELECT count(p.event) as cnt,
  100 * count(p.event)/(SELECT count(p1.event) FROM `prev` p1 WHERE p1.module = 'ransom') as percentage,
  p.f_filename,
  (SELECT p1.f_path FROM `prev` p1 WHERE p1.f_filename = p.f_filename and p.module = 'ransom' GROUP BY p1.f_path ORDER BY count(p1.f_path) DESC limit 1) as f_common
FROM `prev` p
WHERE p.module = 'ransom'
group by p.f_filename
ORDER BY cnt DESC;


- Usefull websites:
  - https://www.w3schools.com/sql/default.asp
  - https://www.db-fiddle.com/





Python chapter:
---------------

Input:
JSON data from https://my-json-server.typicode.com/dim4iksh/test/db

Output:
1. Print a list of file types and count of how many files are there for each type in the database.
2. Print the oldest entry in the list.

Python chapter solution:
------------------------

- Python script created: elb_exercise/json_parser.py


