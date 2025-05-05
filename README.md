# 🚗 Carbeetle Project — AI-Powered Garage Door Automation

Welcome to the **Carbeetle Project**, where artificial intelligence meets home automation. This project leverages computer vision to detect the presence of a specific car and automatically opens the garage door using a Raspberry Pi. It's a seamless blend of AI and IoT, transforming everyday routines into smart experiences.

## 🔧 Project Overview

The Carbeetle system is designed to:

- **Detect a specific vehicle** using real-time computer vision.
- **Trigger the garage door** to open automatically upon detection.
- **Operate autonomously** on a Raspberry Pi, ensuring a compact and efficient setup.

This project exemplifies how AI can be integrated into daily life, enhancing convenience and showcasing the potential of smart home technologies.

## 🧠 How It Works

1. **Model Training**: Utilizing the YOLOv5 object detection framework, the system is trained to recognize the target vehicle from various angles and lighting conditions.

2. **Real-Time Detection**: A camera feed is continuously analyzed by the Raspberry Pi. When the trained model identifies the specific car, it sends a signal to activate the garage door mechanism.

3. **Hardware Control**: The Raspberry Pi interfaces with a relay module connected to the garage door opener, executing the open command safely and reliably.

## 📁 Repository Structure
carbeetle_project/
├── training.py # Script for training the YOLOv5 model
├── yolo11n.pt # Trained YOLOv5 model weights
├── data.yaml # Dataset configuration file
├── runs/ # Directory containing training results
├── saved_models/ # Directory for storing trained models
├── train/ # Training dataset images
├── valid/ # Validation dataset images
├── Carbeetle_pullup.mp4 # Sample video demonstrating the system
├── README.dataset.txt # Notes on dataset preparation
├── README.roboflow.txt # Notes on using Roboflow for dataset management


## 🛠️ Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BaneBeetle/carbeetle_project.git
   cd carbeetle_project
2. **Install Dependencies**:
   Ensure you have Python 3 and pip installed. Then, install the required packages:
   pip install -r requirements.txt
3. **Prepare the Dataset**:
  Collect images of the target vehicle from various angles.
  Annotate the images using a tool like LabelImg.
  Organize the images into train/ and valid/ directories.
4. **Train the Model**:
   python training.py
5. **Deploy on Raspberry Pi**:
  Transfer the trained model (.pt file) to the Raspberry Pi.
  Set up the camera and relay module connections.
  Run the detection script to start the system.

🎥 Demonstration
Check out the system in action:
Carbeetle Testing
https://youtu.be/xfvG6XdplDM
Hardware Testing
https://youtu.be/j32fJZjH9N8

🤝 Acknowledgements
YOLOv11: For the robust object detection framework.
Roboflow: For simplifying dataset management and annotation.
Raspberry Pi Community: For extensive resources on hardware interfacing.

Developed by Brian Phan. For inquiries or collaborations:
phan.brian.minh@gmail.com
www.banebeetle.com
