# Experiments

All experiments underwent training, validation, and testing procedures. The standard commands are outlined in the 
file with the corresponding name, while any deviations are documented below.


## Experiment 1: Transfer learning

```
--data <path_to_project>/objectDetectionVideo/data/processed/ds_ascent_1000/ascent_1000.yaml
--project <path_to_project>/objectDetectionVideo/models/experiments/experiment01
```

### Training

#### Train

```
--epochs 600
--batch-size 64

--freeze 10
```

#### Finetune

```
--epochs 100
--batch-size 64

--weights <path_to_project>/objectDetectionVideo/models/experiments/experiment01/train/weights/best.pt

--hyp <path_to_project>/objectDetectionVideo/models/hyps/hyp.finetune.yaml
--name finetune
```

## Experiment 2: Training from scratch

```
--data <path_to_project>/objectDetectionVideo/data/processed/ds_ascent_1000/ascent_1000.yaml
--project <path_to_project>/objectDetectionVideo/models/experiments/experiment02
```

### Training

```
--epochs 600
--batch-size 64

--weights ''
--cfg <path_to_project>/objectDetectionVideo/models/architectures/pr_yolov5s.yaml
```
