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
python pascalvoc.py -t 0.3
```


## Exercise2: YOLO-V3 inference
--------------------
In this part, we will use pretrained weights to make predictions on both image and video. See [exercise_2_yolov3_inference.ipynb](https://github.com/NCTU-VRDL/tensorflow2_yolov3/blob/master/exercise_2_yolov3_inference.ipynb)

```
$ python3 image_demo.py
```

<p align="center">
    <img width="100%" src="https://user-images.githubusercontent.com/30433053/68088581-9255e700-fe9b-11e9-8672-2672ab398abe.jpg" style="max-width:100%;">
    </a>
</p>

## Exercise3: YOLO-V3 training to detect digits
--------------------
In this part, we will train the YOLO-V3 on the digits dataset and check the performance. See [exercise_3_yolov3_training.ipynb](https://github.com/NCTU-VRDL/tensorflow2_yolov3/blob/master/exercise_3_yolov3_training.ipynb)


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
$ python3 test.py # Inference on the test-set
$ python3 mAP.py # Compute the mAP on test-set (run test.py first)
```
