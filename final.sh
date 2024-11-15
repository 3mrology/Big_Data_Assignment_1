#!/bin/bash

# Define variables
container_name="assignment"
dest_dir="bd-a1/service-result"

# Create the destination directory if it doesn't exist
if [ ! -d "$dest_dir" ]; then
    mkdir -p "$dest_dir"
fi

# Copy files from the container to the local directory
docker cp "$container_name:/home/doc-bd-a1/res_dpre.csv" "$dest_dir/res_dpre.csv"
docker cp "$container_name:/home/doc-bd-a1/eda-in-1.txt" "$dest_dir/eda-in-1.txt"
docker cp "$container_name:/home/doc-bd-a1/eda-in-2.txt" "$dest_dir/eda-in-2.txt"
docker cp "$container_name:/home/doc-bd-a1/eda-in-3.txt" "$dest_dir/eda-in-3.txt"
docker cp "$container_name:/home/doc-bd-a1/vis.png" "$dest_dir/vis.png" 
docker cp "$container_name:/home/doc-bd-a1/k.txt" "$dest_dir/k.txt"

# Stop the container
docker stop "$container_name"

echo "Files copied to $dest_dir and container stopped."

