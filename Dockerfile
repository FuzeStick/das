FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
COPY requirements.txt /home/bot
COPY main.py /home/bot
RUN pip3 install -r /home/bot/requirements.txt
ENTRYPOINT [/usr/local/bin/python3, main.py]
