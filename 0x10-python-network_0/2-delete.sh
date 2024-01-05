#!/bin/bash
# A script that sends a DELETE request to the URL passed as the 1st argument
curl -s "$1" -X DELETE
