Hand Gesture Volume Control 🎵

A Python project that uses computer vision and hand tracking to control music volume through hand gestures. By detecting the number of extended fingers using MediaPipe, the application adjusts the playback volume in real time.

✨ Features

- Real-Time Hand Tracking: Detects hand landmarks using MediaPipe.
- Finger Detection: Counts extended fingers on a detected hand.
- Gesture-Based Volume Control: Adjusts music volume according to the number of raised fingers.
- Live Webcam Feed: Displays the camera feed using OpenCV.
- On-Screen Volume Display: Shows the current volume percentage.
- Background Music Playback: Plays a local audio file continuously.
- Simple Controls: Press "q" to exit the application.

🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- Pygame Mixer

⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install opencv-python mediapipe pygame

📁 Project Structure

hand-gesture-volume-control/
├── main.py
├── Davood Behboodi - Khoshgeleh.mp3
└── README.md

Place your audio file in the same directory as the Python script, or update the file path in the code.

▶️ Usage

1. Install the required dependencies.
2. Connect a webcam to your computer.
3. Place the audio file in the project directory.
4. Run the application:

python main.py

5. Show one hand to the webcam.
6. Raise or lower your fingers to adjust the music volume.
7. Press "q" to close the application.

✋ Gesture Controls

The application detects the four fingers other than the thumb.

Extended Fingers| Volume
0| 10%
1| 25%
2| 50%
3| 75%
4| 100%

The volume is reset to 10% at the beginning of each iteration and then adjusted according to the number of detected extended fingers.

🧠 How It Works

1. Hand Landmark Detection

MediaPipe Hands detects hand landmarks from the webcam feed.

The application examines the landmarks at indices "8", "12", "16", and "20", corresponding to the index, middle, ring, and little fingertips.

2. Finger Counting

For each finger, the application compares the vertical position of the fingertip with the landmark two positions before it.

If the fingertip has a smaller normalized "y" coordinate, the finger is counted as extended.

3. Volume Adjustment

The number of detected extended fingers determines the target volume.

Pygame Mixer applies the selected volume to the currently playing music.

4. Real-Time Display

OpenCV displays the webcam feed and overlays the current volume percentage on the image.

⚠️ Limitations

- The application requires a working webcam.
- The audio file must exist at the specified path.
- Finger detection relies on landmark positions and may be affected by hand orientation, lighting, and occlusion.
- The current implementation tracks one hand and ignores thumb position.
- The volume is controlled through five discrete levels rather than a continuous range.
- The program is designed to control the music played by Pygame Mixer, not the operating system's master volume.

🚀 Possible Improvements

- Add thumb detection to support more gestures.
- Display hand landmarks on the webcam feed.
- Smooth volume transitions to reduce sudden changes.
- Add support for pause, resume, and track switching.
- Allow users to configure gesture-to-volume mappings.
- Add a graphical interface for selecting audio files.
- Improve finger detection for different hand orientations.

📄 License

No license has been specified yet. Add a license file if you intend to define how others may use, modify, or distribute this project.
