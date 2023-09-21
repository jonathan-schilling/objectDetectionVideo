# Dataset

## Download data

As raw data a video with Valorant gameplay became downloaded form the streaming platform Twitch. The video shows a 
match of Valorant professionals playing at the Valorant Champions 2023 in Los Angeles. The best teams of the world 
compete there for the world champions title.

The chosen video shows the game between the european team FNATIC and the american team LOUD in the lower semifinal 
elimination match. They played on three different maps (Ascent, Haven and Split). It was downloaded with the tool 
yt-dlp. The sequences can be found in the folder *data/raw/videos_raw*. And the downloader script is saved in
*scripts/downloader.sh*. That script gets a start and an end timestamp and downloads the given sequence of the
specified video. With that method the original video became downloaded without replays and non-gameplay.

### References

* Video: [https://www.twitch.tv/videos/1907425469](https://www.twitch.tv/videos/1907425469)
* YT-DLP: [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Create frames

The neural networks used will not be trained with video data but with images. That also makes it easier to label the 
data. Therefore, the downloaded video sequences was split into several frames with the *src/data/create_data.py* 
program. It takes the videos as input and saves one frame per second into the target folder *data/interim/frames* 
separated by map. 

## Crop frames

The learning task just works on the in-game mini-map therefore it's useful to crop the map from the whole image. 
That has the nice side effect that the size of the input data for the network reduces. That can be done with the 
program *src/data/crop_data.py*. The cropped maps can than be found in *data/interim/crops*.

## Label data

## Build dataset
