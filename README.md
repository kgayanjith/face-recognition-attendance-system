# 📸 Face Recognition Attendance System

A real-time facial recognition attendance system built with OpenCV. Automatically detects and logs attendance when recognized faces appear on camera.

## ✨ Features

- **Real-time face detection and recognition** using OpenCV's LBPH algorithm
- **Automatic attendance logging** to CSV files with timestamps
- **Apple Silicon optimized** - works perfectly on M1/M2/M3/M4 chips
- **Visual feedback** with bounding boxes and confidence scores
- **Duplicate prevention** - each person recorded only once per session
- **Daily CSV reports** with name and time stamps

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Webcam
- macOS, Windows, or Linux

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

2. Install dependencies:
```bash
pip install opencv-contrib-python numpy
```

3. Set up your photos:
```bash
mkdir photos
# Add photos named: rayan.jpg, kevin.jpeg, shaggy.jpg, president.jpg
```

### Usage

Run the attendance system:
```bash
python app.py
```

- The system will start your webcam and begin detecting faces
- When a known face is detected, attendance is automatically logged
- Press **'q'** to quit
- Attendance is saved to a CSV file named with today's date (e.g., `2025-11-15.csv`)

## 📁 Project Structure

```
face-recognition-attendance-system/
├── app.py                 # Main application
├── photos/                # Store reference photos here
│   ├── rayan.jpg
│   ├── kevin.jpeg
│   ├── shaggy.jpg
│   └── president.jpg
├── YYYY-MM-DD.csv        # Generated attendance logs
└── README.md
```

## 🎯 How It Works

1. **Training Phase**: The system loads reference photos and trains an LBPH face recognizer
2. **Detection**: Uses Haar Cascade to detect faces in real-time video
3. **Recognition**: Matches detected faces against trained models
4. **Logging**: Records name and timestamp when confidence threshold is met

## ⚙️ Configuration

### Adding New People

1. Add their photo to the `photos/` folder (formats: .jpg, .jpeg, .png)
2. Update the `known_faces_names` list in `app.py`:
```python
known_faces_names = ["rayan", "kevin", "shaggy", "president", "newperson"]
```

### Adjusting Recognition Sensitivity

Modify the confidence threshold (default: 70):
```python
if confidence < 70:  # Lower = stricter matching
```

## 📊 CSV Output Format

```csv
Name,Time
rayan,14:32:15
kevin,14:32:48
shaggy,14:33:22
```

## 🐛 Troubleshooting

### "No faces loaded"
- Ensure photos are in the `photos/` folder
- Check that filenames match exactly (case-sensitive)
- Verify photos contain clear, frontal faces

### Low recognition accuracy
- Use well-lit, clear photos
- Ensure faces are clearly visible and frontal
- Try adjusting the confidence threshold
- Add multiple photos per person for better training

### Camera not working
- Check camera permissions in System Preferences (macOS)
- Try changing camera index: `cv2.VideoCapture(1)` or `(2)`

## 🔧 Technical Details

- **Face Detection**: Haar Cascade Classifier
- **Face Recognition**: Local Binary Patterns Histograms (LBPH)
- **Compatible with**: Apple Silicon (M1/M2/M3/M4), Intel, Windows, Linux

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 💡 Future Enhancements

- [ ] Web interface for managing attendance
- [ ] Multiple camera support
- [ ] Email notifications
- [ ] Database integration
- [ ] Mobile app support
- [ ] Advanced analytics dashboard

## 👤 Author

Your Name - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- Built with OpenCV
- Inspired by modern attendance tracking needs
- Optimized for Apple Silicon performance
