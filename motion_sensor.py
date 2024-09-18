import serial
import cv2
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
is_recording = False
out = None
last_motion_time = None
MOTION_TIMEOUT = 60  # 1 minute

def start_recording():
    global is_recording, out, last_motion_time
    if not camera.isOpened():
        return
    out = cv2.VideoWriter(f'motion_{int(time.time())}.mp4', fourcc, 20.0, (640, 480))
    if not out.isOpened():
        return
    is_recording = True
    last_motion_time = time.time()

def stop_recording():
    global is_recording, out
    if is_recording and out is not None:
        out.release()
    is_recording = False

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8', errors='ignore').rstrip()

        if "Motion detected!" in line:
            last_motion_time = time.time()
            if not is_recording:
                start_recording()

        if "Motion ended!" in line and is_recording:
            if time.time() - last_motion_time >= MOTION_TIMEOUT:
                stop_recording()

    if is_recording:
        ret, frame = camera.read()
        if not ret:
            stop_recording()
        else:
            out.write(frame)
            cv2.imshow('Recording', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                stop_recording()
                break

camera.release()
cv2.destroyAllWindows()
