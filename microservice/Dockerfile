FROM microservice:v0.1

WORKDIR /src

ADD  . .  

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && apt update && apt -y install telnet net-tools curl libmariadb-dev \
    && pip3 install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

CMD [ "python3 manage.py runserver 0.0.0.0:8080" ]
