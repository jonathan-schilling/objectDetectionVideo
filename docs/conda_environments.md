# Anaconda Python Environments

This project uses three separate Python environments managed via Anaconda.

## Development Environment

This environment is used for developing and using the programs under `src`.

```
conda create --name projectPr
conda activate projectPr

conda install nodejs
conda install -c conda-forge jupyterlab
conda install -c conda-forge opencv
```

## Label Studio

This environment is needed to use Label Studio.

```
conda create --name labelStudio
conda activate labelStudio

conda install pip

conda install -c anaconda pyqt
conda install -c anaconda lxml
conda install psycopg2

pip install label-studio
```

### Start Label Studio

First of all Label Studio has to be initialized, after that it can be started.

```
label-studio init
label-studio start --username "<name>@localhost" --password "<changeme>"
```

## YOLOv5

This environment is needed to use YOLOv5. Due to issues with CUDA it was necessary to install an older 
version of PyTorch and that needed also an older version of Python.

```
conda create --name train39 python=3.9
conda activate train39

conda install pip
```

The following command has to be executed in the base folder of the YOLOv5 repository.

```
pip install -r requirements.txt
```

Per default a CPU version of PyTorch is installed. To activate GPU support the PyTorch version has to be changed.

```
pip uninstall torch torchvision

pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
```
