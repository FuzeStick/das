FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get -y install python3-pip
COPY main.py /home/bot/
WORKDIR /home/bot/
ENTRYPOINT [/usr/local/bin/python3, kop.py]
