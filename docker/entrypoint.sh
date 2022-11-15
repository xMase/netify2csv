#!/bin/bash

set -e

socat_tmp_file=/app/output/tmp-output.csv
netify_sock=/var/run/netifyd/netifyd.sock

netifyd --thread-detection-cores=1 -d -t --wait-for-client -I lo,$input &

until [ -S $netify_sock ]
do
     sleep 5
done

socat - UNIX-CONNECT:$netify_sock > $socat_tmp_file
python -u main.py --input $socat_tmp_file --output $output