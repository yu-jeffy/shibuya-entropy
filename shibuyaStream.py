import subprocess

def download_frame(video_id='Tw2RYnTXuy8', output_file='shibuya.jpg'):
    try:
        # Run yt-dlp to get the video URL
        yt_dlp_command = ['yt-dlp', '-g', video_id]
        yt_dlp_output = subprocess.run(yt_dlp_command, capture_output=True, text=True, check=True)

        # Get the first URL from the output
        video_url = yt_dlp_output.stdout.split('\n')[0]
        
        # Run ffmpeg to capture the first frame of the video
        ffmpeg_command = ['ffmpeg', '-i', video_url, '-vframes', '1', output_file, '-y']
        subprocess.run(ffmpeg_command, check=True)

        print(f"Frame saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_frame()

