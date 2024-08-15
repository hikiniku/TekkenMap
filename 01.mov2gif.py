from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(mp4_path, gif_path, image_path, fps, start_time=None, end_time=None):
    """
    Convert MP4 video to GIF.
    
    :param mp4_path: Path to the input MP4 video file.
    :param gif_path: Path to save the output GIF file.
    :param start_time: Start time in seconds for the GIF (optional).
    :param end_time: End time in seconds for the GIF (optional).
    """
    # Load the video clip
    video_clip = VideoFileClip(mp4_path)
    
    # Trim the video if start_time and end_time are provided
    if start_time and end_time:
        video_clip = video_clip.subclip(start_time, end_time)

    #resolution = (1280, 720) 
    resolution = (640, 360) 
    # Resize the video clip to the specified resolution
    video_clip = video_clip.resize(newsize=resolution)

    video_clip.save_frame(image_path, t=(start_time if start_time else 0))
    
    # Write the video clip as GIF
    video_clip.write_gif(gif_path, fps)

# Example usage
mp4_path = 'boot_RK.mp4'
gif_path = 'boot_RK.gif'
image_path = 'first_frame.png'
start_time = 2  # Start at 2 seconds
end_time = 5    # End at 5 seconds
fps = 15

#convert_mp4_to_gif(mp4_path, gif_path, fps, start_time, end_time)
convert_mp4_to_gif(mp4_path, gif_path, image_path, fps)

