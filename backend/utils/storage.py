import boto3
from config.settings import settings

session = boto3.session.Session()

client = session.client(
    "s3",
    endpoint_url=settings.CLOUDFLARE_R2_ENDPOINT,
    aws_access_key_id=settings.CLOUDFLARE_R2_ACCESS_KEY,
    aws_secret_access_key=settings.CLOUDFLARE_R2_SECRET_KEY
)

def upload_file(file_path, key):
    client.upload_file(file_path, settings.CLOUDFLARE_R2_BUCKET, key)
    return f"{settings.CLOUDFLARE_R2_ENDPOINT}/{settings.CLOUDFLARE_R2_BUCKET}/{key}"
