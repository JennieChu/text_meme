#!/usr/bin/env bash
filename="$1"
while read line
do
    website="http://apimeme.com/meme?meme=$line&top=&bottom="
    wget "$website"
done < "$filename"