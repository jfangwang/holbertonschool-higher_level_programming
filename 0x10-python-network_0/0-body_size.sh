
#!/bin/bash
# Displays the size of the body response

if [ $# -eq 1 ];then
    curl -s "$1" | wc -c
fi
