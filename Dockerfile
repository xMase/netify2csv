FROM centos:7

WORKDIR /app

ENV netify_file netifyd-4.3.5-1.os7.x86_64.rpm

ENV input $input
ENV output $output

ENV PYTHONUNBUFFERED=1

RUN yum install -y socat python3-pip

COPY . /app

RUN yum localinstall -y /app/res/${netify_file} 

RUN chmod +x docker/entrypoint.sh

ENTRYPOINT ["/app/docker/entrypoint.sh"]
