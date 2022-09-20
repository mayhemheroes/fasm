# Build Stage
FROM debian:buster as builder

RUN apt update && apt install -y fasm python3

## Add source code to the build stage.
ADD . /src
WORKDIR /src

RUN python3 mayhem/lower.py && \
    fasm -m 1000000 source/linux/x64/fasm.asm /fasm && chmod +x /fasm

# Package Stage
FROM debian:buster

COPY --from=builder /fasm /
