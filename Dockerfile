FROM jupyter/scipy-notebook

RUN pip install dateparser==0.7.2 lxml==4.4.1 cufflinks==0.16

WORKDIR /app
