# Сборка Free Pascal в докере через lazarus-build-station
# (https://github.com/attid/lazarus-build-station) + слой с клиентом Firebird.
FROM ghcr.io/attid/lazarus-build-station:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends libfbclient2 \
    && rm -rf /var/lib/apt/lists/* \
    # FPC 3.2.2 ищет жёстко зашитые имена libfbclient.so.2.5.1 / libgds.so,
    # а Debian ставит клиент с новым soname — линкуем старое имя на реальную
    # библиотеку (soname находим через ldconfig).
    && REAL="$(ldconfig -p | awk '/libfbclient\.so\.[0-9]/ {print $NF; exit}')" \
    && ln -s "$REAL" /usr/lib/x86_64-linux-gnu/libfbclient.so.2.5.1 \
    && ldconfig

WORKDIR /app
COPY main.pas .
RUN fpc -FE. main.pas

CMD ["./main"]
