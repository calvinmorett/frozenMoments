#frozenmoments.py
import os
import shutil

# store the merged frames in this new directory
os.makedirs('merged_frames', exist_ok=True)

# set  number of videos and intervals
num_videos = int(input("Enter the number of videos: "))  # Update this value according to the number of videos you have
video_intervals = [5, 5, 5]  # Update this list with the intervals for each video

# iterate over frames, in sets, per max_interval value
max_interval = max(video_intervals)

for i in range(1, 40, max_interval):
    for video_index in range(num_videos):
        interval = video_intervals[video_index]
        for j in range(interval):
            frame_index = i + j
            video_frame_index = (frame_index - 1) % interval + 1
            video_frame_path = f'video{video_index + 1}_frame{video_frame_index:03d}.jpg'
            merged_frame_index = (i - 1) * num_videos + sum(video_intervals[:video_index]) + j + 1
            shutil.copy(video_frame_path, f'merged_frames/frozenmoment_frame{merged_frame_index:03d}.jpg')
