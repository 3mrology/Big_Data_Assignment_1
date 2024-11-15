FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1

COPY . /home/doc-bd-a1

WORKDIR /home/doc-bd-a1

CMD ["/bin/bash"]
