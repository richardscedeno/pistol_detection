import cv2
from ultralytics import YOLO
import imutils
import funciones

model = YOLO('./weights/best50.pt')

# video_path = "./data/vid1.mp4"
# cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    frame_copy = frame.copy()
    frame_copy = imutils.resize(frame_copy, width=500)

    if success:
        results = model(frame)

        # Guardando la confidecialidad del tensor
        conf = results[0].boxes.conf
        # print(f'conf: {conf}')
        # print(type(conf))

        plot_frame = results[0].plot()

        cv2.imshow("YOLOv8", plot_frame)

        if conf.nelement() != 0:
            print(f'Tiene datos: {conf.nelement()}')
            funciones.validate_route()
        else:
            print(f'Está vacio: {conf.nelement()}')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
