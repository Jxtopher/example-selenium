FROM python:3.7.13-alpine

RUN apk --update \
    add --no-cache alpine-sdk git icu-data-full curl firefox \
    && pip install black mypy flake8 selenium requests webdriver_manager  \
    && addgroup -S user && adduser -S user -G user -s /bin/ash \
    && echo "user    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  \
    && echo "user:password" | chpasswd

RUN echo -e "from webdriver_manager.firefox import GeckoDriverManager\nGeckoDriverManager().install()" | python 

ENTRYPOINT ["su", "user"]
