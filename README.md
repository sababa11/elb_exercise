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


