#!/bin/bash

s="$1" ## start timestamp
e="$2" ## end timestamp
n="$3" ## output name

yt-dlp --external-downloader ffmpeg --external-downloader-args "ffmpeg_i:-ss "$s".00 -to "$e".00" --output ""$n".mp4" https://www.twitch.tv/videos/1907425469
