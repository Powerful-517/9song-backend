import oss2

from app.config import OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_ENDPOINT, OSS_BUCKET_NAME


auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)


# Generate a URL for file upload
def get_upload_url(file_name: str):
    # Expire time is 10 minutes
    # Must set "Content-Type" correctly
    url = bucket.sign_url('PUT', file_name, 10 * 60, slash_safe=True, headers={"Content-Type": "audio/mpeg"})
    return url


# Generate a URL for file download
def get_download_url(file_name: str):
    url = bucket.sign_url('GET', file_name, 10 * 60, slash_safe=True)
    return url


# Determine if a file exists
def is_file_exists(file_name: str):
    exist = bucket.object_exists(file_name)
    return exist
