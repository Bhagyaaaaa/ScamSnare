 🛡️ ScamSnare

An AI-powered scam detection tool that helps identify fraudulent content across WhatsApp, YouTube, and other social media platforms. ScamSnare analyzes text, links, images, and videos to detect potential scams and protect users from online fraud.

## 🎯 Purpose

With the rise of digital scams, phishing attempts, and fake news, ScamSnare provides a quick and easy way to verify suspicious content before engaging with it. Whether it's a "too good to be true" offer, a suspicious link, or a deepfake video, ScamSnare helps users stay safe online.

## ✨ Features

- **Text & Link Analysis**: Detects suspicious keywords and patterns in messages and URLs
- **Image Detection**: Analyzes uploaded images for potential scam indicators
- **Video Detection**: Checks video content for fake or manipulated media
- **Real-time Results**: Instant feedback on whether content is likely real or fake
- **Simple Interface**: Clean, user-friendly web interface
- **Multi-platform Support**: Works with content from WhatsApp, YouTube, social media, and more

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **Python 3.x**: Core programming language
- **CORS Middleware**: Cross-origin resource sharing support

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling
- **Vanilla JavaScript**: Interactivity and API calls

## 📁 Project Structure

```
ScamSnare/
├── Backend/
│   └── main.py              # Enhanced backend with improved logic
├── main.py                  # Primary backend server
├── index.html               # Frontend interface
├── script.js                # Client-side logic
├── style.css                # Styling
└── __pycache__/             # Python cache files
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhagyaaaaa/ScamSnare.git
   cd ScamSnare
   ```

2. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn python-multipart
   ```

3. **Start the backend server**
   ```bash
   # Using the main.py file
   uvicorn main:app --reload --port 8000
   
   # OR using the Backend version
   cd Backend
   uvicorn main:app --reload --port 8000
   ```

4. **Open the frontend**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     python -m http.server 3000
     ```
   - Navigate to `http://localhost:3000`

## 📖 How to Use

### Analyze Text/Links

1. Paste the suspicious text or link in the input field
2. Click "Analyze"
3. View the result: "Looks Safe!" (green) or "Warning! Scam detected" (red)

### Analyze Images/Videos

1. Click "Choose File" and select an image or video
2. Click "Analyze"
3. Wait for the analysis result

## 🔍 Detection Methods

### Current Implementation (Demo Version)

**Text/Link Analysis:**
- Checks for suspicious keywords: "free money", "lottery", "100% guaranteed", "win big"
- Random classification for ambiguous content (to be replaced with ML model)

**Image/Video Analysis:**
- File size-based heuristic (demo logic)
- Files < 50KB flagged as potentially fake
- Placeholder for future ML-based deepfake detection

### Planned Enhancements

- **Machine Learning Models**: Integration of trained models for scam detection
- **NLP Analysis**: Natural language processing for advanced text analysis
- **Deepfake Detection**: AI-powered image and video manipulation detection
- **URL Reputation Check**: Cross-reference links with known scam databases
- **Pattern Recognition**: Identify common scam patterns and structures

## 🔧 API Endpoints

### POST `/check`

Analyzes uploaded content for scam indicators.

**Request:**
- **Form Data**:
  - `file` (optional): Image or video file
  - `link` (optional): Text or URL to analyze

**Response:**
```json
{
  "result": "Real" | "Fake"
}
```

**Error Response:**
```json
{
  "error": "No file or link provided."
}
```

## 🔒 Security Considerations

⚠️ **Important for Production:**

1. **CORS Configuration**: Update `allow_origins` to specify exact domains instead of `["*"]`
2. **Rate Limiting**: Implement rate limiting to prevent API abuse
3. **File Validation**: Add strict file type and size validation
4. **Authentication**: Consider adding API keys or user authentication
5. **HTTPS**: Deploy with SSL/TLS encryption
6. **Input Sanitization**: Sanitize all user inputs to prevent injection attacks
7. **File Storage**: Implement secure temporary file storage with cleanup

## 🚧 Current Limitations

- Detection logic is currently based on simple heuristics (demo version)
- Random classification for ambiguous cases
- No persistent storage or history
- Limited to basic keyword matching for text
- File size-based detection for media (placeholder)

## 🎯 Future Roadmap

- [ ] Integrate machine learning models (TensorFlow/PyTorch)
- [ ] Add deepfake detection for images and videos
- [ ] Implement NLP-based text analysis
- [ ] Create database for known scam patterns
- [ ] Add user authentication and history tracking
- [ ] Build browser extension for real-time protection
- [ ] Mobile app development (iOS/Android)
- [ ] Multi-language support
- [ ] API for third-party integrations
- [ ] Real-time link reputation checking
- [ ] Reporting system for new scams
- [ ] Admin dashboard for monitoring

## 🤝 Contributing

Contributions are welcome! This project is perfect for adding ML models and improving detection accuracy.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add ML-based scam detection'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution

- ML model integration
- Deepfake detection algorithms
- NLP improvements
- UI/UX enhancements
- Testing and validation
- Documentation

## 💡 Use Cases

- **Personal Safety**: Verify suspicious messages before clicking links
- **Elderly Protection**: Help vulnerable users identify scams
- **Business Security**: Screen incoming messages and emails
- **Education**: Teach users about common scam patterns
- **Research**: Study scam trends and patterns

## 🧪 Testing

Currently in **MVP/Demo stage**. To test:

1. Try text with keywords: "free money lottery win" → Should flag as Fake
2. Try normal text: "Hello, how are you?" → Random or Real
3. Upload small image (< 50KB) → Should flag as Fake
4. Upload large image (> 50KB) → Should flag as Real

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Bhagyaaaaa**
- GitHub: [@Bhagyaaaaa](https://github.com/Bhagyaaaaa)

## 🙏 Acknowledgments

- FastAPI documentation and community
- Online fraud prevention resources
- Open source ML communities

## 📞 Support

If you encounter any issues or have suggestions:
- Open an issue on GitHub
- Submit a pull request
- Contact the maintainer

---

⭐ **Stay Safe Online!** If this project helps you, please give it a star!

**Disclaimer**: This tool is for educational and demonstration purposes. It should not be solely relied upon for security decisions. Always exercise caution with suspicious content.
