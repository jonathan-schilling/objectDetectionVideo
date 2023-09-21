"""
Convert video into frames (one frame per second)

by Jonathan Schilling
"""

import cv2

from src import paths as p


def video2frames(map_name, video_name, next_frame_name):
    video = cv2.VideoCapture(str(p.DATA_BASE_DIR / p.VIDEO_DIR / map_name / (video_name + p.VIDEO_FORMAT)))

    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    frame_name = next_frame_name
    frame_nr = 0
    saved_frames = 0

    # save frames
    while True:
        success, frame = video.read()

        if success:
            # save one frame per second
            if frame_nr % fps == 0:
                cv2.imwrite(
                    str(p.DATA_BASE_DIR / p.FRAME_DIR / map_name / ('frame_' + str(frame_name) + p.IMAGE_FORMAT)),
                    frame)
                saved_frames += 1
        else:
            break

        frame_nr += 1
        frame_name += 1

    video.release()

    log = f"Map: {map_name}, Video: {video_name}, #Frames: {num_frames}, FPS: {fps}, #savedFrames: {saved_frames}"
    print(log)

    return frame_name, saved_frames, log
