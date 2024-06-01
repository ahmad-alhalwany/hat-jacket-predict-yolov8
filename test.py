from ultralytics import YOLO

model = YOLO("yolov8m_custom.pt")

model.predict( source='1.jpeg.jpeg', show=True, save=True, conf=0.5 )