#!/bin/sh
LARGE_SECRET_PASSPHRASE=<ASK THE AUTHOR FOR PASSPHRASE>

# decrypt firebase secret
LARGE_SECRET_PASSPHRASE=bangkit.red-hat.predict-cc
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output firebase-service-account.json secret.gpg

# decrypt ml
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ml.zip ml.zip.gpg
7za x -aoa -p$LARGE_SECRET_PASSPHRASE ml.zip
rm ml.zip


