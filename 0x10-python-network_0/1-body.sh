#!/bin/bash
# A script to get the body of the response
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ];
then curl -Ls "$1";
fi
