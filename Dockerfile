From typesense/typesense:0.22.2
WORKDIR /usr/src
RUN apt-get update -y && apt-get install curl -y;curl -O https://dl.typesense.org/datasets/books.jsonl.gz
