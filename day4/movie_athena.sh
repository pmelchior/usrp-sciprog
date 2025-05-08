#!/bin/bash
PID=OrszagTang
for i in `ls -d $PID.out2.00*.athdf`
do
    echo $i
    ../vis/python/plot_slice.py $i press slice_$i.png --colormap plasma --vmin 0.0 --vmax 0.36 
done
echo "converting to animated gif"
convert -delay 1 slice_$PID.*.png $PID.gif
rm -rf slice_$PID*
