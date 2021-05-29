#!/bin/sh

# Deploy to heroku
git add . && git commit -m ":rocket: Deploy to heroku"
git push -f heroku master

# Cleanup
git reset --hard HEAD~1