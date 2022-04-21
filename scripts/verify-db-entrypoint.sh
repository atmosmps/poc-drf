#!/bin/sh

echo "Waiting MongoDB start..."

while ! nc -z db 27017; do
  sleep 0.1
done

echo "MongoDB started"

exec "$@"
