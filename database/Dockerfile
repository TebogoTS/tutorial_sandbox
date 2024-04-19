# Dockerfile for MySQL
FROM mysql:5.7

# Environment variables for MySQL
ENV MYSQL_DATABASE=people_db
ENV MYSQL_ROOT_PASSWORD=password

# Adding database schemas and scripts
ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306
