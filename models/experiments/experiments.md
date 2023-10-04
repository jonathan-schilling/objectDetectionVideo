# Experiments

All experiments underwent training, validation, and testing procedures. The standard commands are outlined in the 
file with the corresponding name, while any deviations are documented below. The first two experiments were also 
trained using the Adam optimizer, with all other settings held constant. You can find the training results in the 
`experiments/adam` subfolder, though they were not evaluated further.

## Experiment 1

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_500/ascent_500.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex1
```

### Training

```
--epochs 150
--batch-size 32
```

## Experiment 2

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_500/ascent_500.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex2
```

### Training

```
--epochs 150
--batch-size 64
```

## Experiment 3: Fine-tuning

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_500/ascent_500.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex3   
```

### Training

#### Train

```
--epochs 150
--batch-size 64

--freeze 10
```

#### Finetune

```
--epochs 50
--batch-size 64

--weights C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex3/train/weights/best.pt

--hyp C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/hyps/hyp.finetune.yaml
--name finetune
```

## Experiment 4a: Train from scratch

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_1000/ascent_1000.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex4a
```

### Training

```
--epochs 300
--batch-size 64

--weights ''
--cfg C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/architectures/pr_yolov5s.yaml
```

## Experiment 4b

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_1000/ascent_1000.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex4b
```

### Training

#### Train

```
--epochs 150
--batch-size 64

--freeze 10
```

#### Finetune

```
--epochs 100
--batch-size 32

--weights C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex4b/train/weights/best.pt

--hyp C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/hyps/hyp.finetune.yaml
--name finetune
```

## Experiment 5: Overfitting

```
--data C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/data/processed/ds_ascent_1000/ascent_1000.yaml
--project C:/Users/Jonathan/Documents/Development/git/gitlab/projectpr/models/experiments/ex5
```

### Training

```
--epochs 600
--batch-size 64

--save-period 20
```
