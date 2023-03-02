# err-exportboy

## Clone this code to errbot plugins path


## Setup environment for 

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