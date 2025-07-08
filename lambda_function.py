from PIL import Image
import boto3
import os
import tempfile

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    destination_bucket = 'chea-image-resized'

    download_path = os.path.join(tempfile.gettempdir(), key)
    upload_path = os.path.join(tempfile.gettempdir(), f"resized-{key}")

    s3.download_file(source_bucket, key, download_path)

    with Image.open(download_path) as img:
        img = img.resize((128, 128))
        img.save(upload_path)

    s3.upload_file(upload_path, destination_bucket, f"resized-{key}")

    return {
        'statusCode': 200,
        'body': f"Image resized and uploaded to {destination_bucket}"
    }

