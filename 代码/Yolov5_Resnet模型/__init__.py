from Detect_and_Track.get_tracks import get_video_tracks
from Detect_and_Track.create_tracking_boxes_video import create_tracking_boxes_video

#call get_video_tracks with path of any football match footage,
# for more info see Detect_and_Track/get_tracks file
#the function would save new clean video without zoomed in frames in "Out/" folder with the chosen name
get_video_tracks(video_path, output_video_name)

#and to create the video with tracking boxes around players
#the function would save new video with playerrs/ball tracked -each with unique ID-, in "Out/" folder with the chosen name
create_tracking_boxes_video(video_path, output_video_name)