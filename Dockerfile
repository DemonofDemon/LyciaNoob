FROM debian:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg python3-pip curl
RUN python3 -m pip install -U pip

COPY . .

RUN git clone https://github.com/theheirofzeus/shit /root/fuck

RUN python3 -m pip install -U -r /root/fuck/requirements.txt

CMD ["python3", "main.py"]
