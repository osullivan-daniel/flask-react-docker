FROM python:latest

WORKDIR /usr/src/api

COPY requirments.txt ./

RUN python3 -m pip install --user --no-cache-dir -r requirments.txt

COPY . .

CMD ["python3", "server.py"]