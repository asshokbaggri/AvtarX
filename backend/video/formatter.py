import uuid
from utils.ffmpeg import run_ffmpeg
from utils.storage import upload_file

def format_video(video_path):
    output_file = f"/tmp/final_{uuid.uuid4()}.mp4"

    cmd = f"""
        ffmpeg -i {video_path} \
        -vf "scale=1080:1920:force_original_aspect_ratio=decrease,
             pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" \
        -r 30 \
        -y {output_file}
    """

    run_ffmpeg(cmd)

    key = f"videos/{uuid.uuid4()}.mp4"
    url = upload_file(output_file, key)

    return url
