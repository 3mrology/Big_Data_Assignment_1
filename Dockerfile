FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pandas \
        python3-numpy \
        python3-seaborn \
        python3-matplotlib \
        python3-sklearn \
        python3-scipy && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/doc-bd-a1
WORKDIR /home/doc-bd-a1

COPY . /home/doc-bd-a1

CMD ["/bin/bash"]
