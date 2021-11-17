FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip && pip3 install –upgrade pip
COPY requirements.txt /home/bot/
COPY main.py /home/bot/
WORKDIR /home/bot/
RUN pip3 install -r requirements.txt
ENTRYPOINT [/usr/local/bin/python3, main.py]
