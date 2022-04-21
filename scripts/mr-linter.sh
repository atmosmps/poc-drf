#!/usr/bin/env bash

title=$(echo -n "$1")
title_size=$(echo -n "$1" | wc -c)

PATTERN=$(echo "$title" | grep -oEi "\s(\[STK[[:digit:]]+\]+|\[OPS[[:digit:]]+\]+|\[BUG[[:digit:]]+\]+|\[IMP[[:digit:]]+\])$")

if [[ $title_size -gt 73 ]]
then
    echo "==========================";
    echo "MR title must not be longer than 73 characters, current length is $title_size";
    echo "==========================";
    exit 1;
fi

if [[ -z "${PATTERN}" ]]
then
    echo "==========================";
    echo "MR title must contain '*\s[STK|OPS|BUG|IMP+CARD_NUMBER]$' pattern, current is '$title'";
    echo "==========================";
    exit 1;
fi

echo "==========================";
echo "MR title passed the commit lint"
echo "==========================";
