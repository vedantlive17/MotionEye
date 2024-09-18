# MotionEye

This project uses a Raspberry Pi, Arduino with a PIR motion sensor, and a camera to create a system that detects motion and records video. When motion is detected, the system starts recording for at least 1 minute. If motion continues to be detected before the minute ends, the recording continues. The system stops recording only if no motion is detected for a continuous minute.

## Features

- **Motion Detection**: Uses a PIR motion sensor connected to an Arduino.
- **Automatic Video Recording**: Starts recording when motion is detected and continues recording for at least 1 minute.
- **Smart Timeout**: If motion continues during the last minute, the recording continues until no motion is detected for 1 minute.
- **Real-time Video Display**: The camera feed is displayed in real-time while recording.
- **Video Files**: Videos are saved in `.mp4` format with unique timestamps for each recording.

## Components

- **Raspberry Pi**: For controlling the camera and handling video recording.
- **Arduino**: For detecting motion via the PIR sensor.
- **PIR Motion Sensor**: Connected to the Arduino to detect movement.
- **Camera**: Captures video when motion is detected (e.g., a Logitech camera).
- **Libraries**:
  - Python 3
  - OpenCV for video capturing and writing
  - PySerial for serial communication between Arduino and Raspberry Pi

## Setup Instructions

### Hardware Setup

1. **Arduino and PIR Motion Sensor**:
   - Connect the PIR sensor's **VCC** to the **5V** pin on the Arduino.
   - Connect the PIR sensor's **OUT** to digital pin **2** on the Arduino.
   - Connect the PIR sensor's **GND** to the **GND** pin on the Arduino.

2. **Arduino to Raspberry Pi**:
   - Use a USB cable to connect the Arduino to the Raspberry Pi.
   - The Raspberry Pi will read data from the Arduino over the serial connection.

3. **Camera**:
   - Connect a USB camera (e.g., Logitech) to the Raspberry Pi.

### Software Setup

1. **Install Dependencies**:

   Run the following commands on your Raspberry Pi to install the necessary Python libraries:

   ```bash
   sudo apt update
   sudo apt install python3-pip python3-opencv
   pip3 install pyserial
