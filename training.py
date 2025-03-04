# Brian Phan
# 84609992

from ultralytics import YOLO

def main():
    model = YOLO("yolo11m.pt")
    model.train(
        data="C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\data.yaml",  # path to yaml file  
        imgsz=640,  # image size for training  
        batch=8,   # batch size  
        epochs=100,  # number of epochs  
        device=0   # use GPU if available, else CPU
    )

def main1():
    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\detect\\train3\\weights\\best.pt")
    model.predict(source="test//images//carbeetle_00218259_jpg.rf.67814291d0af6e198b432712ba88cc82.jpg", show = True, save = True, line_width = 2)
if __name__ == "__main__":
    main1()

