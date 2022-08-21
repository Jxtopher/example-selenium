FROM python:3.7.13-alpine

RUN apk --update \
    add --no-cache icu-data-full curl firefox \
    && pip install selenium requests webdriver_manager  \
    && addgroup -S user && adduser -S user -G user -s /bin/ash \
    && echo "user    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  \
    && echo "user:password" | chpasswd

ADD --chown=user:user ./main.py /apps/main.py

RUN echo -e "from webdriver_manager.firefox import GeckoDriverManager\nGeckoDriverManager().install()" | python 

ENTRYPOINT ["python", "/apps/main.py"]
