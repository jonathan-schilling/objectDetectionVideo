# Experiments

All experiments underwent training, validation, and testing procedures. The standard commands are outlined in the 
file with the corresponding name, while any deviations are documented below.


## Experiment 1: Transfer learning + freeze

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_1000/ascent_1000.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/experiment01
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

--weights C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/experiment01/train/weights/best.pt

--hyp C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/hyps/hyp.finetune.yaml
--name finetune
```

## Experiment 2: Training from scratch

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_1000/ascent_1000.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/experiment02
```

### Training

```
--epochs 600
--batch-size 64

--weights ''
--cfg C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/architectures/pr_yolov5s.yaml
```
