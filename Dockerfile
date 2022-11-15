FROM centos:7

ENV input $input
ENV output $output

RUN rpm --import http://download.netify.ai/netify/centos/`rpm --eval '%{centos_ver}'`/stable/RPM-GPG-KEY-netify
RUN curl http://download.netify.ai/netify/centos/`rpm --eval '%{centos_ver}'`/netify.repo -o /etc/yum.repos.d/netify.repo
RUN yum install -y netifyd socat python3-pip nc

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN chmod +x docker/entrypoint.sh

ENTRYPOINT ["/app/docker/entrypoint.sh"]
