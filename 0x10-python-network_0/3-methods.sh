#!/bin/bash
#  displays all HTTP methods the server will accept.
curl -sD - -o /dev/null "$1" | tail -n 2 | head -n 1 | cut -b 8-
