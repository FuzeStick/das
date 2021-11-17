FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
WORKDIR /usr/local/bin/
RUN pip3 install vk_api && pip3 install lxml && pip3 install bs4 && pip3 install requests
COPY main.py
ENTRYPOINT [/usr/local/bin/python3, main.py]
