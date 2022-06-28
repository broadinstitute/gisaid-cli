FROM python:3.7

LABEL maintainer "Daniel Park <dpark@broadinstitute.org>"

WORKDIR /opt/gisaid

COPY requirements.txt /opt/gisaid/
RUN pip3 install -r /opt/gisaid/requirements.txt

COPY gisaid_cli3 /opt/gisaid/gisaid_cli3/
RUN pip3 install /opt/gisaid/gisaid_cli3

RUN cli3 -h

CMD ["/bin/bash"]
