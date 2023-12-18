FROM python:3.9-slim
RUN mkdir -p /liwei/test
COPY requirements.txt /liwei/test
COPY app.py /liwei/test
WORKDIR /liwei/test
RUN apt-get update
RUN apt-get install -y build-essential cmake
RUN apt-get install -y libopenblas-dev liblapack-dev
RUN apt-get install -y libx11-dev libgtk-3-dev
RUN apt-get install -y python3-dev python3-numpy python3-pip
RUN pip3 install --no-cache-dir -r ./requirements.txt

EXPOSE 9080
CMD [ "python3", "app.py", "9080" ]