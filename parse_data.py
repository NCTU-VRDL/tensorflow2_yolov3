import glob

cls_dict = {"rectangle":0,
       "circle":1,
       "triangle":2,}

train_path = [os.path.abspath(x) for x in sorted(glob.glob("./data/dataset/train/*.png"))]
with open("data/dataset/train/labels.json") as f:
  train_label = json.load(f)

with open("data/dataset/shape_train.txt", "w") as wf:
  for i, image in enumerate(train_label):
    annotation = train_path[i]
    for obj in image['boxes'][1:]: 
      annotation += ' ' + ','.join(
          [str(obj['x1']), str(obj['y1']),
           str(obj['x2']), str(obj['y2']), str(cls_dict[obj['class']])])
    wf.write(annotation + "\n")


test_path = [os.path.abspath(x) for x in sorted(glob.glob("./data/dataset/test/*.png"))]
with open("data/dataset/test/labels.json") as f:
  test_label = json.load(f)

with open("data/dataset/shape_test.txt", "w") as wf:
  for i, image in enumerate(test_label):
    annotation = test_path[i]
    for obj in image['boxes'][1:]: 
      annotation += ' ' + ','.join(
          [str(obj['x1']), str(obj['y1']),
           str(obj['x2']), str(obj['y2']), str(cls_dict[obj['class']])])
    wf.write(annotation + "\n")


