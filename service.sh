docker build -t searchengine-dev .
docker run -it -p 8108:8108 -v/C/workspace/code/searchdocker/data:/data searchengine-dev --data-dir /data --api-key=Hu52dwsas2AdxdE