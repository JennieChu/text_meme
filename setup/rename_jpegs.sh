#!/usr/bin/env bash

for entry in `ls`; do
    mv $entry ${entry#meme?meme=}
done

for entry2 in `ls`; do
    mv $entry2 ${entry2%&top=&bottom=}
done
