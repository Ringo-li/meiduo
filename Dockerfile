FROM harbor.example.com/library/python:3.7-slim
LABEL auth="ringo" 

WORKDIR /data/app

COPY requirements.txt .

RUN  sed -i 's/deb.debian.org/ftp.cn.debian.org/g' /etc/apt/sources.list \
  && sed -i 's/security.debian.org/ftp.cn.debian.org/g' /etc/apt/sources.list \
  && apt-get update -y \
  && apt-get install -y wget gcc libsm6 libxext6 libglib2.0-0 libxrender1 make \
  && apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt \
    && rm requirements.txt

COPY . .

EXPOSE 8000
# HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT ["python", "meiduo_mall/manage.py", "runserver", "0.0.0.0:8000"]