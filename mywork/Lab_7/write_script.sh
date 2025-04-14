#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <local_file> <bucket_name> <expiration 
	in seconds>
	exit 1
fi 
	
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

aws s3 cp "$LOCAL_FILE" s3://"$BUCKET_NAME"/ --acl private

if [ $? -ne 0 ]; then
	echo "upload failed"
	exit 2
fi


PRESIGNED_URL=$(aws s3 presign s3://"$BUCKET_NAME"/"$(basename "$LOCAL_FILE")" --expires-in "$EXPIRATION")

if [ $? -ne 0 ]; then
	echo "failed to make url presigned"
	exit 3
fi

echo "file uploaded"
echo "Presigned URL (expires in $EXPIRATION seconds):"
echo "$PRESIGNED_URL"
