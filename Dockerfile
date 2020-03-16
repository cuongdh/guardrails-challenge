FROM python:3-alpine
RUN addgroup -S nodejsscan && adduser -S nodejsscan -G nodejsscan -s /bin/false
WORKDIR /usr/src/app

# Copy required files from host to image
COPY ./build/cli.requirements.txt ./
COPY ./build/core ./core
RUN mkdir -p /usr/src/app/test-src
RUN chown -R nodejsscan:nodejsscan /usr/src/app
USER nodejsscan
# Install required dependencies
RUN pip install --no-cache-dir -r cli.requirements.txt \
    # Move cli.py from /usr/src/app/core to /usr/src/app
    && mv ./core/cli.py .

ENTRYPOINT ["python","/usr/src/app/cli.py"]

