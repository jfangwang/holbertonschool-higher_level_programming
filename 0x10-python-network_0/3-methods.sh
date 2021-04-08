#!/bin/bash
#  displays all HTTP methods the server will accept.
curl -sI "$1" | tail -n 2 | head -n 1 | cut -d ' ' -f 2-
