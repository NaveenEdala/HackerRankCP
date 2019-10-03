read -n 1 query

if [ "$query" == "Y" ] || [ "$query" == "y" ]; then
    echo "YES"
elif [ "$query" == "N" ] || [ "$query" == "n" ]; then
    echo "NO"
fi
