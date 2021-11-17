FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
WORKDIR /usr/local/bin/
COPY requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py
ENTRYPOINT [/usr/local/bin/python3, main.py]
