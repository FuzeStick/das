FROM python3
COPY requirements.txt
RUN pip install --user -r requirements.txt
CMD [ 'python main.py' ]
