# FileIntegrity-monitoring
This project implements a file integrity monitoring (FIM) System on  Kali Linux to detect unauthorized file changes using SHA-256 hashing   
It includes multi-user permission management to simulate insider threats and privilege abuse.

### 📌 OBJECTIVES 
- Monitor file Integrity
- Detect file modification or deletion
- Generate alert logsg
- Simulate bleu-team security monitoring

### 🏭 Environment
- OS: Kali Linux
- language: Python 3
- Hashing Algorithm : SHA-26
  
### 📁 Monitored Files 
- '/FileIntegrity-monitoring/file1.conf'
- '/FileIntegrity-monitoring/file2.conf'
- '/FileIntegrity-monitoring/file3.conf'
- '/FileIntegrity-monitoring/file4.conf'
- '/FileIntegrity-monitoring/file5.conf'
- '/FileIntegrity-monitoring/file6.conf'
Each file is owned by a different Linux user and protected with restrictive permissions.

### ✔ How It Works
1 - The script calculates SHA-256 Hashes of monitored files
2 - Hashes are stored in a baseline database
3 - On each execution, new hashes are compared with the baseline
4 - Any modification, detection, or new file triggers an alert 

### 🚀 Usage
````bash
python3 FIM-monitoring.py
````
