# err-exportboy

## Clone this code to errbot plugins path
```bash
git clone https://github.com/wxlee/err-exportboy.git
```

## Setup environment 

FILE: /etc/systemd/system/errbot.service

Change the Environment to yours.

```bash

[Unit]
Description=Start Errbot chatbot
After=network.service

[Service]
Environment="LC_ALL=en_US.UTF-8"
Environment="PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/home/errbotuser/.venv/bin"
Environment="JENKINS_USER_TOKEN=..."
Environment="JENKINS_PRJ_TOKEN=..."
Environment="JENKINS_URL=...:8080"
ExecStart=/home/errbotuser/.venv/bin/errbot --config /home/errbotuser/chatops/config.py
WorkingDirectory=/home/errbotuser/chatops
User=errbotuser
Restart=always
KillSignal=SIGINT

[Install]
WantedBy=multi-user.target

```

## Setup service

```bash
systemctl daemon-reload
systemctl start errbot.service
systemctl enable errbot.service
```

## Setup supervisor (for docker)

FILE:/etc/supervisor/conf.d/errbot.conf

```bash
[supervisord]
environment=JENKINS_USER_TOKEN="...",JENKINS_PRJ_TOKEN="...",JENKINS_URL="...:8080"
[program:errbot]
command = /home/errbotuser/.venv/bin/errbot --config /home/errbotuser/chatops/config.py
user = errbotuser
stdout_logfile = /var/log/supervisor/errbot.log
stderr_logfile = NONE
redirect_stderr = true
directory = /home/errbotuser/chatops
startsecs = 3
stopsignal = INT
environment = LC_ALL="en_US.UTF-8"

```

## Startup service
```bash
systemctl enable supervisor
systemctl restart supervisor
```
