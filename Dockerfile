FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get -y install python3-pip
COPY main.py /home/bot/
WORKDIR /home/bot/
RUN pip3 install vk_api && pip3 install lxml && pip3 install bs4 && pip3 install requests
ENTRYPOINT [/usr/local/bin/python3, main.py]
