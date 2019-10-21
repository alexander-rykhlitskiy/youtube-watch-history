FROM jupyter/scipy-notebook:1386e2046833

RUN pip install dateparser==0.7.2 lxml==4.4.1 cufflinks==0.16

WORKDIR /app
