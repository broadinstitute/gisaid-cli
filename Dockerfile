FROM python:3.7

LABEL maintainer "Daniel Park <dpark@broadinstitute.org>"

WORKDIR /opt/gisaid

COPY requirements.txt gisaid_cli3 /opt/gisaid

RUN pip3 install -r /opt/gisaid/requirements.txt
RUN pip3 install /opt/gisaid/gisaid_cli3

#ENV PATH="$PATH:/opt/gisaid/scripts"

#COPY . /opt/gisaid

RUN cli3 -h

CMD ["/bin/bash"]
