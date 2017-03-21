#!/bin/bash
set -e

input_list=`cat $1`

for f in $input_list;
do
  mkdir -p `dirname $f`
  http -d https://commoncrawl.s3.amazonaws.com/$f -o $f
done
