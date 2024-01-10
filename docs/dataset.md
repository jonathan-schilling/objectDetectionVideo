# Dataset

## Download data

As raw data a video with Valorant gameplay became downloaded from the streaming platform Twitch. The video shows a match of Valorant professionals playing at the Valorant Champions 2023 in Los Angeles. The best teams of the world compete there for the world champions title.

The chosen video shows the game between the european team FNATIC and the american team LOUD in the lower semifinal elimination match. They played on three different maps (Ascent, Haven and Split). It was downloaded with the tool yt-dlp. The sequences can be found in the folder `data/raw/videos_raw`. And the downloader script is saved in `scripts/downloader.sh`. That script gets a start and an end timestamp and downloads the given sequence of the specified video. With that method the original video became downloaded without replays and non-gameplay.

### References

* Video: [https://www.twitch.tv/videos/1907425469](https://www.twitch.tv/videos/1907425469)
* YT-DLP: [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Create frames

The neural networks will not be trained with video data but with images. That makes it easier to label the 
data. Therefore, the downloaded video sequences were split into several frames with the `src/data/create_data/create_data.py` program. It takes the videos as input and saves one frame per second into the 
target folder `data/interim/frames` separated by map. 

## Crop frames

The learning task just works on the in-game mini-map therefore it's useful to crop the map from the whole image. 
That has the nice side effect that the size of the input data for the network reduces. That can be done with the 
program `src/data/create_data/crop_data.py`. The cropped maps can than be found in `data/interim/crops`. Each image 
has the size `384x384 Pixels`.

## Label data

The cropped mini-maps become labeled using the open source data labeling platform [Label Studio](https://labelstud.io/). Therefore the label template in `data/interim/labels/template` is used. With that template it's possible to set a point in the middle of each entity that should be labeled. Using those settings labeled data can be created efficiently. The labeled data becomes exported to `JSON`.

## Build dataset

For training, the [YOLOv5](https://github.com/ultralytics/yolov5) neural network is used. That AI comes with its own format of a dataset and uses squares around each entity as label shape. For efficiency reasons the data became labeled with a point in the center, therefore the created labels have to be parsed into YOLO format. That is being done with the program `src/data/build_yolo_dataset.py`.

## Training

As described before, videos of the maps Ascent, Haven and Split are available. Due to the reason that labeling data is very time consuming the videos of all maps were prepared as cropped images but only 1000 Ascent images became labeled. Therefore the neural networks only were trained with images of Ascent.

## Inference

The best performing neural network was used for inference on new data (that hasn't been used for training). The results of the detection task can be found in `models/experiments/experiment01/detect`. Because of the fact that the neural network only was trained for Ascent the focus of detection lays also on this map. To check the networks generalization ability it was additionally applied on a video of the map Haven. The results of that test were very satisfying. Not as good as those from Ascent but already usable as it can be seen in `models/experiments/experiment01/detect/vid_haven/result_heatmap.png`.
