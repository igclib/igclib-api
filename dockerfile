FROM ubuntu:18.04
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates python3-dev python3-pip python3-setuptools build-essential libspatialindex-dev
RUN pip3 install wheel

RUN git clone https://github.com/teobouvard/igclib.git 
WORKDIR /igclib
RUN pip3 install -e .

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD [ "gunicorn", "--bind", "0.0.0.0", "web.api:app" ]