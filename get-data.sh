#!/bin/bash
set -e

input_list=`cat $1`

for f in $input_list;
do
  echo "Downloading $f"
  mkdir -p `dirname $f`
  if [ ! -f $f ]; then
    http -d https://commoncrawl.s3.amazonaws.com/$f -o $f
  fi
done
