FROM microservice:v0.1

WORKDIR /src

ADD  . .  

RUN pip3 install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

ENTRYPOINT ["./entrypoint.sh"]
