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


Python chapter:
---------------

Input:
JSON data from https://my-json-server.typicode.com/dim4iksh/test/db

Output:
1. Print a list of file types and count of how many files are there for each type in the database.
2. Print the oldest entry in the list.

