NBA IFTTT Close Game Alert
====

Python script to send an IFTTT notification for NBA close game situations.

Run as a cron job and linked to MongoDB to keep track of notification status.


Dockerfile
----
```docker
ENV DB_CONN_STRING ''
ENV MAKER_URL ''
```