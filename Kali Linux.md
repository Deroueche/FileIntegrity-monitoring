## File Integrity Monitoring 
### Part 01 : Environment Setup (Kali Linux)
#### 🔹CREATE 3 users:
````bash
bash:
$ sudo su
# adduser awatif
New password:
# adduser akram
New password:
# adduser asma
New password:
````
verify 
````bash
bash
# id awatif
#id akram
#id asma
````
#### 🔹create monitoring directory & files permissions:
````bash
bash
$ sudo mkdir /FileIntegrity-monitoring
$ sudo touch /FileIntegrity-monitoring/file1.conf /FileIntegrity-monitoring/file2.conf /FileIntegrity-monitoring/file3.conf /FileIntegrity-monitoring/file4.conf /FileIntegrity-monitoring/file5.conf /FileIntegrity-monitoring/file6.conf
````
#### 🔹Add content:
````bash
bash
$ echo "Database configuration" | sudo tee file1.conf
$ echo "Firewall Rules" | sudo tee file2.conf
$ echo "System policy" | sudo tee file3.conf
$ echo "Networking configuration" | sudo tee file4.conf
$ echo "SIEM Configuration" | sudo tee file5.conf
$ echo "IPS System" | sudo tee file6.conf
````
#### 🔹Ownership and permissions:

|  Users  |  Role     |  Permission  |
|---------|-----------|--------------|
|  awatif |   Admin   |  Read/write  |
|  Akram  |  Editor   |  Write only  |
|  Asma   | Viewer    |   Read only  |






````bash
bash
$ cd FileIntegrity-monitoring
$ sudo chmod awatif:awatif /FileIntegrity-monitoring/file1.conf
$ sudo chmod 600 file1.conf
````
verify:
````bash
bash
$ ls -l file1.conf
-rw---------------awatif awatif      file1.conf
````










  

