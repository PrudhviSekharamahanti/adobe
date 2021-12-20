# Adobe Data Analytics

**Data File: data.tsv**
Attached is a simple tab separated file which contains what we call "hit level data". A hit level record is a single "hit" from a visitor on the client's site. Based on the client's implementation, several variables can be set and sent to Adobe Analytics for deeper analysis.

Steps:
1. create a Docker image of the application using command
    docker build -t <imagename> .
2. Create AWS EC2 instance:
    https://www.guru99.com/creating-amazon-ec2-instance.html
3. Connect to EC2 instance and install and start docker service using following commmands
    sudo yum install docker -y
    sudo service docker start
4. Create Inbound rule for HTTP
5. Login to docker hub
    sudo docker login
6. Pull docker image
    docker pull <repname>:imagename
7. Run Docker image on EC2 using the command
    docker run -d -p 80:8501 <imagename>
8. Access the application using public DNS of EC2