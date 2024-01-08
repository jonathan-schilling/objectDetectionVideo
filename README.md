# Object detection on videos using YOLOv5

An individual project as part of the Computer Science Master's program at the University of Ulm.

## Project Description

The scope of this project was to gain experience in the usage of an existing machine learning model (YOLOv5 [1]) on own data. The main goal was to analyze player behaviour from a video game (Valorant). Due to the reason that the only public available data is accesible via screen captures, the YOLOv5 model was trained to detect player icons on a map that is shown in the game for overview reasons. The training was performed on images, while the trained model can be applied on recorded videos. As example output for an analysis a simple heatmap was chosen.

The first challenge was to prepare suitable data and label a sufficient amount of images. As second challenge several training setups were tested and network configurations for transfer learning and training from scratch were found. The dataset with most images (1000) was applied and satisfying results could be achived. Thereby the transfer learning task performed best.

Next to the machine learning framework You Only Look Once (YOLO) the labeling application Label Studio [2] was used.

<br><br><br>
[1] Glenn Jocher. YOLOv5 by Ultralytics. May 2020. DOI: [10.5281/zenodo.3908559](10.5281/zenodo.3908559).<br>
[2] Label Studio - Open Source Data Labeling. URL: [https://labelstud.io/](https://labelstud.io/).

## Project Structure

```
├── README.md
│
├── data
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- Final datasets & data for prediction tasks
│   └── raw            <- Original, immutable data 
│
├── docs
│
│── models             <- Model data for/from training/validation/testing
│
├── notebooks          <- Jupyter notebooks 
│
├── scripts            <- Scripts 
│
└── src                <- Source code
    └── data           <- Scripts generate datasets
```

