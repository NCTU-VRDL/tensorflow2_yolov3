## [TensorFlow2.x-YOLOv3](https://yunyang1994.github.io/posts/YOLOv3/#more)
--------------------
A minimal tensorflow implementation of YOLOv3, with support for training, inference and evaluation.

## Installation
--------------------
Install requirements and download pretrained weights

```
$ pip3 install -r ./docs/requirements.txt
$ wget https://pjreddie.com/media/files/yolov3.weights
```


## Exercise1: Evaluation
In this part, we will practice how to compute the average precision of our model.
```
cd exercise1
python pascal_voc.py -t 0.3
```


## Exercise2: YOLO-V3 inference
--------------------
In this part, we will use pretrained weights to make predictions on both image and video.

```
$ python3 image_demo.py
```

<p align="center">
    <img width="100%" src="https://user-images.githubusercontent.com/30433053/68088581-9255e700-fe9b-11e9-8672-2672ab398abe.jpg" style="max-width:100%;">
    </a>
</p>

## Exercise2: YOLO-V3 training to detect digits
--------------------

<p align="center">
    <img width="70%" src="https://user-images.githubusercontent.com/30433053/68088705-90d8ee80-fe9c-11e9-8e61-589fdc45fe60.png" style="max-width:70%;">
    </a>
</p>



- Open `./core/config.py` and do some configurations
```
__C.YOLO.CLASSES                = "./data/classes/yymnist.names"
```

- Finally, you can train it and then evaluate your model

```
$ python3 train.py
$ python3 test.py
```
