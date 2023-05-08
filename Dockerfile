FROM amd64/ubuntu:18.04
# FROM ubuntu:18.04

USER root

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


ENV DEBIAN_FRONTEND=noninteractive
RUN set -x \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends wget git gcc make build-essential sudo tor libnss3-dev libgconf2-4 \
    && apt-get install -y --no-install-recommends libnss3-dev libgconf2-4  libnss3 unzip libx11-6 gnupg python3-selenium language-pack-ja-base language-pack-ja \
    #&& apt-get install -y --no-install-recommends psmisc net-tools bzip2 unzip vim \
    && rm -rf /var/lib/apt/lists/*

RUN set -x \
    apt-get update -y && \
    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet --no-check-certificate https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH="/opt/conda/bin:$PATH"

RUN ls
RUN apt-get update -y
RUN apt-get install -y libappindicator1 curl
ENV DISPLAY=:0.0


RUN apt-get install -y language-pack-ja-base language-pack-ja
RUN locale-gen ja_JP.UTF-8
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja
ENV LANG=ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8

RUN apt install -y fonts-takao
RUN fc-cache -fv
RUN fc-match TakaoGothic
RUN apt install -y fonts-ipafont fonts-ipaexfont
RUN fc-cache -fv
RUN fc-match IPAGothic

RUN mkdir -p /var/task/bin/

RUN apt install -y chromium-browser
RUN apt install -y chromium-chromedriver

RUN apt install python3-selenium

RUN mkdir -p /opt/.fonts/
RUN wget --quiet https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip
RUN unzip IPAexfont00401.zip -d /opt/.fonts/
RUN mv /opt/.fonts/IPAexfont00401/ipaexg.ttf /opt/.fonts/
RUN mv /opt/.fonts/IPAexfont00401/ipaexm.ttf /opt/.fonts/
RUN rm -rf /opt/.fonts/IPAexfont00401
RUN fc-cache -fv


COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN pip install \
    --target /usr/src/app/\
        awslambdaric


COPY ./app /usr/src/app/


ENTRYPOINT [ "python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]