#!/usr/bin/env bash
set -e

echo "Creating skills folder..."
mkdir -p static/img/skills

BASE="https://raw.githubusercontent.com/devicons/devicon/master/icons"

echo "Downloading language icons..."
curl -L "$BASE/cplusplus/cplusplus-original.svg"        -o static/img/skills/cpp.svg
curl -L "$BASE/java/java-original.svg"                 -o static/img/skills/java.svg
curl -L "$BASE/c/c-original.svg"                       -o static/img/skills/c.svg
curl -L "$BASE/python/python-original.svg"             -o static/img/skills/python.svg
curl -L "$BASE/html5/html5-original.svg"               -o static/img/skills/html.svg
curl -L "$BASE/css3/css3-original.svg"                 -o static/img/skills/css.svg
curl -L "$BASE/javascript/javascript-original.svg"     -o static/img/skills/javascript.svg
curl -L "$BASE/mysql/mysql-original-wordmark.svg"      -o static/img/skills/sql.svg

echo "Downloading tools & tech icons..."
curl -L "$BASE/react/react-original.svg"               -o static/img/skills/react.svg
curl -L "$BASE/django/django-plain.svg"                -o static/img/skills/django.svg
curl -L "$BASE/flask/flask-original.svg"               -o static/img/skills/flask.svg
curl -L "$BASE/bootstrap/bootstrap-original.svg"       -o static/img/skills/bootstrap.svg
curl -L "$BASE/git/git-original.svg"                   -o static/img/skills/git.svg
curl -L "$BASE/linux/linux-original.svg"               -o static/img/skills/linux.svg
curl -L "$BASE/oracle/oracle-original.svg"             -o static/img/skills/oracle.svg
curl -L "$BASE/express/express-original.svg"           -o static/img/skills/express.svg
curl -L "$BASE/amazonwebservices/amazonwebservices-original.svg" -o static/img/skills/aws.svg
curl -L "$BASE/spring/spring-original.svg"             -o static/img/skills/spring.svg

echo "✅ All icons downloaded into static/img/skills/"
