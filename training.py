# Brian Phan
# 84609992

from ultralytics import YOLO

def train():
    '''In charge of training and fine-tuning YOLOv11 to distinguish Carbeetle from Civilians.'''

    model = YOLO("yolo11m.pt")
    model.train(
        data="C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\data.yaml",  # path to yaml file  
        imgsz=640,  # image size for training  
        batch=8,   # batch size  
        epochs=100,  # number of epochs  
        device=0   # use GPU if available, else CPU
    )

def test_on_image():
    '''Function that tests on a specified image path rather than webcam.'''

    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\detect\\train3\\weights\\best.pt")
    model.predict(source="test//images//carbeetle_00218259_jpg.rf.67814291d0af6e198b432712ba88cc82.jpg", show = True, save = True, line_width = 2) 


def webcam_testing():
    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\detect\\train3\\weights\\best.pt") # Load up the fine-tuned model

    model.predict(
        source=0,         # 0 for the default webcam --- the one pointed outside my house
        imgsz=640,        # image size 
        conf=0.84,        # confidence threshold
        show=True,        # display the results live
        save=True,        # optionally save the output video/images
        line_width=2      # line width for drawing bounding boxes
    )

if __name__ == "__main__":
    
    webcam_testing()
