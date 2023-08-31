#!/bin/bash
# HTTP methods
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
