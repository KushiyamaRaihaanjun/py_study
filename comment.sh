#!/bin/bash
git add .
read COMMENT
git commit -m "$COMMENT"
git push origin master