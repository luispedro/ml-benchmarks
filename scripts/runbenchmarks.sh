#!/bin/bash

mkdir -p results
for bench in benchmarks/bench_*py ; do
    bname=`basename $bench .py | cut -d_ -f2`
    echo "running $bname..."
    python $bench > results/$bname.txt
done

