from datetime import datetime
import random, time, os

OUT = "/var/log/splunk_test/syslog_like.log"
HOST = "parrot"

GOOD_IPS = ["192.168.1.10", "192.168.1.11"]
BAD_IPS  = ["192.168.1.100", "192.168.1.101", "192.168.1.102", "192.168.1.103", "10.0.0.15"]
USERS    = ["root", "jay"]

def now():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")

def gen_line():
    user = random.choice(USERS)
    if random.random() < 0.6:
        # Accepted login
        src_ip = random.choice(GOOD_IPS)
        port = random.randint(1024, 65000)
        return f"{now()} {HOST} sshd[{random.randint(3000,4000)}]: Accepted password for {user} from {src_ip} port {port} ssh2"
    else:
        # Failed login (now includes port)
        src_ip = random.choice(BAD_IPS)
        port = random.randint(1024, 65000)
        return f"{now()} {HOST} sshd[{random.randint(6000,7000)}]: Failed password for {user} from {src_ip} port {port} ssh2"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

N = 12
for _ in range(N):
    line = gen_line().strip()
    with open(OUT, "a") as f:
        f.write(line + "\n")
    print(line)
    time.sleep(0.2)
