# Brian Phan
# 84609992

from ultralytics import YOLO
import cv2
import time

def train():
    '''In charge of training and fine-tuning YOLOv11 to distinguish Carbeetle from Civilians.'''

    model = YOLO("yolo11m.pt")
    model.train(
        data="C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\data.yaml",  # path to yaml file  
        imgsz=640,  # image size for training  
        batch=16,   # batch size  
        epochs=200,  # number of epochs  
        device=0   # use GPU if available, else CPU
    )


def test_on_image():
    '''Function that tests on a specified image path rather than webcam.'''

    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\\detect\\train3\\weights\\best.pt")
    model.predict(source="test//images//carbeetle_00218259_jpg.rf.67814291d0af6e198b432712ba88cc82.jpg", show = True, save = True, line_width = 2) 

    return None

def webcam_testing():
    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\\detect\\train\\weights\\best.pt") # Load up the fine-tuned model

    model.predict(
        source=0,         # 0 for the default webcam --- the one pointed outside my house
        imgsz=640,        # image size 
        conf=0.30,        # confidence threshold
        show=True,        # display the results live
        save=True,        # optionally save the output video/images
        line_width=2      # line width for drawing bounding boxes
    )

    return None

def webcam_testing2():
    # Load the fine-tuned model
    model = YOLO("C:\\Users\\lolly\\OneDrive\\Desktop\\Projects\\carbeetle_project\\runs\\detect\\train\\weights\\best.pt")
    
    # Open the default webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run inference on the frame
        results = model(frame, conf=0.70)  # use the lower global threshold

        # Assuming results[0].boxes.data is structured as [x1, y1, x2, y2, confidence, class_id]
        if results and results[0].boxes is not None:
            detections = results[0].boxes.data.tolist()
            for detection in detections:
                x1, y1, x2, y2, conf, class_id = detection
                class_id = int(class_id)
                label = model.names[class_id]

                if label == "Carbeetle" and conf < 0.88:
                    continue
                if label == "Carbeetle" and conf >= 0.88:
                    print("Hi Carbeetle!")

                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    text = f"{label}: {conf:.2f}"
                    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.9, (255, 0, 255), 2)

                elif label == "Civilian" and conf < 0.30:
                    continue
                
                # Draw bounding box and label on the frame
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                text = f"{label}: {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.9, (0, 0, 255), 2)

        # Display the processed frame
        cv2.imshow("Live Feed - Custom Filter", frame)
        
        # Exit out of webcam testing if pressing Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #train()

    webcam_testing2()
