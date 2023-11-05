FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=qwerty123
ENV POSTGRES_DB=pgproject

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

# docker build -t <nama image>:<tag> <direktori dokcerfile>