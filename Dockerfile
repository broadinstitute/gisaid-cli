FROM python:3.7

LABEL maintainer "Daniel Park <dpark@broadinstitute.org>"

WORKDIR /opt/gisaid

COPY requirements.txt /opt/gisaid

RUN pip3 install -r /opt/gisaid/requirements.txt

ENV PATH="$PATH:/opt/gisaid/scripts"

COPY . /opt/gisaid

RUN gisaid_uploader --help

CMD ["/bin/bash"]