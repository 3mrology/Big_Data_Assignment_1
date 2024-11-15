# How to use



## Hover over to the directory



```bash
cd "assignment 1"
```

## Build docker image
This create a docker image called assignment1. The "." specifies that the dockerfile is in the directory
```cmd
docker build -t assignment1 .
```

## Running the container
This command create a docker container named assignment. The -it flag allows the user to interact with the bash shell inside the container
```cmd
docker run -it --name assignment assignment1
```
As soon as you start the container you will be in the working directory (/home/doc-bd-a1)

## Inside the container
This will start the pipeline for the analysis
```cmd
python3 load.py Mall_Customers.csv
```

## Finish
After completing the pipeline exit the container
```cmd
exit
```
## Copying the items to the Host os
You will need to run the final.sh script
```cmd
./final.sh
```

## Bonus
Tagging the image so we can push it
```cmd
docker tag assignment1:latest 3mrology/bonus:1.0 
```
Pushing the image
```cmd
docker push 3mrology/bonus:1.0 
```