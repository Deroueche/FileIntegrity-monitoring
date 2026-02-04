import hashlib
import os
import time
from datetime import datetime


FILES_TO_MONITOR = [
   "/FileIntegrity-monitoring/file4.conf",
   "/FileIntegrity-monitoring/file5.conf",
   "/FileIntegrity-monitoring/file6.conf"
   ]
HASH_DB = "hashes.db"
LOG_FILE = "alerts.log"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
          for block in iter(lambda: f.read(4096), b""):
              sha256.update(block)
    return sha256.hexdigest()

def load_hashes():
    hashes = {}
    if os.path.exists(HASH_DB):
       with open(HASH_DB, "r") as f :
           for line in f:
               file, hash_value = line.strip().split("|")
               hashes[file] = hash_value
    return hashes
def save_hashes(hashes):
    with open(HASH_DB, "w") as f:
         for file, hash_value in hashes.items():
             f.write(f"{file}|{hash_value}\n")
def log_alert(messages):
    with open(LOG_FILE, "a") as log:
         log.write(f"{datetime.now()} ALERT: {messages}\n")

def main():
    print("[+] Starting File Integrity Monitoring...")
    stored_hashes = load_hashes()
    current_hashes = {}

    for file in FILES_TO_MONITOR:
        if os.path.exists(file):
           current_hashes[file] = calculate_hash(file)
           if file not in stored_hashes: 
              log_alert(f"New file detected: {file}")
           elif stored_hashes[file] != current_hashes[file]:
                log_alert(f"File modified: {file}")
                print(f"[!] ALERT: {file} modified")
        else:
             log_alert(f"File detected: {file}")
             print(f"[!] ALERT: {file} detected")

    save_hashes(current_hashes)

if __name__ == "__main__":
     main()
