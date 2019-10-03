total=0
read N

for i in $(seq 1 $N); do
    read intx
    total=$(( $total + $intx ))
done

printf "%.3f\n" `echo "$total / $N" | bc -l`
