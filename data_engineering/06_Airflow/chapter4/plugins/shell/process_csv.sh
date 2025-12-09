#!/bin/bash

data=(
    "1, John@!, 28"
    "2, Alice#$, 32"
    "3, Bob%^, 25"
    "4, Alice#$, 32"
    "5, Eve&*, 29"
)

echo "Starting data processing..."

echo "Original Data:"
for row in "${data[@]}"; do
    echo "$row"
done

echo "Processing Data..."
processed_data=()
for row in "${data[@]}"; do
    clean_row=$(echo "$row" | tr -d ' ' | tr '[:lower:]' '[:upper:]' | sed 's/[^A-Z0-9,]//g')
    processed_data+=("$clean_row")
done

echo "Removing Duplicates & Sorting..."
sorted_data=($(printf "%s\n" "${processed_data[@]}" | sort -u))

echo "Final Processed Data:"
for row in "${sorted_data[@]}"; do
    echo "$row"
done

echo "Data processing completed!"