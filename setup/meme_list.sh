#!/usr/bin/env bash
curl http://apimeme.com/ | grep "option" | cut -d'>' -f2 | cut -d'<' -f1 | grep -v '^[0-9]' | grep -v '^[a-z][0-9]' | grep -v 'memebot' | grep -v 'Screen' | grep -v 'RackMulti' |tr ' ' '+' > page_source.txt
