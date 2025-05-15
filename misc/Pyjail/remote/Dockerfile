FROM python:3.9

RUN apt-get update && apt-get install -y socat

WORKDIR /app
COPY app/ /app

RUN echo '#!/bin/sh\nstty -echo\nexec python /app/app.py' > /app/launch.sh && chmod +x /app/launch.sh
RUN useradd -ms /bin/bash appuser
USER appuser

CMD socat TCP-LISTEN:6005,reuseaddr,fork EXEC:"/app/launch.sh"