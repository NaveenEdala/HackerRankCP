awk '{
    if ( NR % 2 == 1 )
        printf "%s;", $0
    else
        printf "%s\n", $0  
}'
