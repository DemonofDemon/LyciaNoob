FROM debian:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg python3-pip curl git
RUN python3 -m pip install -U pip


RUN git clone https://github.com/theheirofzeus/shit /root/fuck

RUN python3 -m pip install -U -r /root/fuck/requirements.txt

WORKDIR /root

CMD ["python3","main.py"]
