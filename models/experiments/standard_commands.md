## Standard commands

The subsequent commands were used for training, validation and testing using the corresponding dataset splits.

### Training

```
python train.py

	--epochs <NUM_EPOCHS>
	--batch-size <BATCH_SIZE>
	
	--weights yolov5s.pt
	--img 384
	--optimizer SGD

	--data <PATH_TO_DATASET>.yaml
	--project <PATH_TO_PROJECT>
	--name train
	
	--cache ram
	--device cuda:0
	--save-period 10
```

### Validation

```
python val.py

	--weights <PATH_TO_PROJECT>/train/weights/best.pt

	--data <PATH_TO_DATASET>
	--project <PATH_TO_PROJECT>
	--name validation

	--batch-size 64
	--task val
		
	--save-txt
	--save-conf
	
	--augment
	--device cuda:0
```

### Test

```
python val.py

	--weights <PATH_TO_PROJECT>/train/weights/best.pt

	--data <PATH_TO_DATASET>
	--project <PATH_TO_PROJECT>
	--name test

	--batch-size 64
	--task test
		
	--save-txt
	--save-conf
	
	--augment
	--device cuda:0
```

### Inference

This command can be used for inference. It's possible to apply the neural network to image and video data. The 
`save-crop` option is not recommended for use with video inputs.

```
python detect.py

	--weights <PATH_TO_PROJECT>/train/weights/best.pt

	--source <PATH_TO_DATA>
	--project <PATH_TO_PROJECT>/detect
	--name <NAME_OF_DETECT_TASK>
	
	--conf-thres 0.8
	
	--augment
	--line-thickness 2
	--hide-labels
	--view-img
	--save-txt
	--save-conf
	--device cuda:0
	

	(--save-crop)
```
