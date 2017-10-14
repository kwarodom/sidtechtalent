FROM python:3.6.2

RUN apt-get update -y
RUN pip install --upgrade pip
# Install ML related
RUN pip install numpy scipy matplotlib pandas
# Install django
RUN pip install django djangorestframework
# more packages
RUN pip install scikit-learn

WORKDIR /home
RUN django-admin startproject sidtechtalent
WORKDIR /home/sidtechtalent

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

