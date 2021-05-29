#!/bin/sh

# firebase
gpg --yes --quiet --output secret.gpg --batch --pinentry-mode=loopback --passphrase="$LARGE_SECRET_PASSPHRASE" --symmetric --cipher-algo AES256 firebase-service-account.json
rm firebase-service-account.json

# ml
7za a -tzip -p$LARGE_SECRET_PASSPHRASE -mem=AES256 ml.zip ml
gpg --yes --quiet --output  ml.zip.gpg --batch --pinentry-mode=loopback --passphrase="$LARGE_SECRET_PASSPHRASE" --symmetric --cipher-algo AES256 ml.zip
rm ml.zip
rm -rf ml
