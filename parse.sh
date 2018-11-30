#!/bin/bash

function usage(){
    echo "Usage: ./parse.sh [FILE]..."
    echo "Cleans FILE to out file"
    echo ""
    echo "Examples:"
    echo "  ./parse.sh data.json"
    echo "  ./parse.sh *.json"
    echo ""
    echo "Facebook JSON Parser"
    echo "This was made for PortAISociety. Feel free to use it for whatever you want."
    echo "More info about the society at: PortAISociety.com"
    echo "Feel free to improve this script at : github.com/PortAISociety/msgGeneratorRNN"
}

function parse(){
    cat $1 | egrep '(sender_name)|(content)' | sed 's/"sender_name": /From: /g' | sed 's/"content": //g' | sed -e 's/[",]//g' | sed -e 's/  //g' |  sed -e 's/\(\(https\)\|\(http\)\):.*/sent a link/g' | sed -e 's/\\u....//g' | sed -e 's/[0-9]//g' | sed -e 's/\\n/\n/g' | sed 's/\[.*//g' | sed -e 's/!*!/!/g' | sed -e 's/?*?/?/g' | sed -e 's/\./\n/g' | sed 's/[^a-z A-Z ?!]//g' | sed -e 's/^ *//g' | sed 's/ *$//g' | sed -e 's/^$/emoji/g' | sed -e 's/^From.*/\0:/g' | sed -e 's/[^:!?]$/\0\./g' | tr '[:lower:][:upper:]' '[:lower:][:lower:]' >> out
}

if [  $# -le 0 ]; then
    usage
    exit 1
else
    >out
    for file in "$@"
    do
        parse $file
    done
fi
