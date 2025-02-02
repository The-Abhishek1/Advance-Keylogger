# Advanced Keylogger

![Keylogger Banner](https://assets.enterprisenetworkingplanet.com/uploads/2023/03/what-is-a-keylogger-768x512.png)  

An advanced keylogger that captures keystrokes, clipboard information, microphone recordings, system information, and screenshots, and sends all the data to a specified email address.

## 🚨 Disclaimer

This tool is for **educational purposes** and **ethical hacking** only. The author does not condone or promote malicious use of this tool. Unauthorized use of this software may violate local, state, or federal laws. Use responsibly and only with explicit permission.

---

## 📋 Features

- **Keystroke Logging**: Captures all typed keys on the system.
- **Clipboard Monitoring**: Tracks and logs clipboard activity.
- **Microphone Recording**: Records audio from the system microphone.
- **System Information Retrieval**: Gathers system details such as OS, hardware info, and more.
- **Screenshot Capture**: Takes screenshots of the system at defined intervals.
- **Email Delivery**: Sends all collected information to a pre-configured email address.

---

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.x
- Internet connection
- SMTP-enabled email account (e.g., Gmail, Outlook)

### Dependencies

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### Configuration

1. Clone the repository:

```bash
git clone https://github.com/yourusername/advanced-keylogger.git
cd advanced-keylogger
```

2. Configure your email and password:

```python
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
```

3. Run the script:

```bash
python keylogger.py
```

---

## 📧 Email Configuration

- Ensure that "Allow less secure apps" is enabled in your email settings (for Gmail users).
- Alternatively, use an **App Password** for better security.
- Ensure your email provider allows SMTP connections.

---

## 🖥️ Usage

1. Run the keylogger on the target system.
2. Data will be logged and sent to the configured email at defined intervals.
3. To stop the keylogger, terminate the process.

---

## 🔒 Ethical Considerations

This tool should only be used:
- For testing your own systems.
- With explicit permission from the system owner.

Unauthorized use is strictly prohibited.

---

## 📄 License


MIT License

Copyright (c) 2025 Abhishek Gowda

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


---

## 📂 File Structure

```
advanced-keylogger/
│
├── keylogger.py        # Main keylogger script
├── config.py           # Configuration file for email credentials
├── requirements.txt    # List of required Python libraries
├── README.md           # Project documentation (this file)
└── LICENSE             # License file
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## 📞 Contact

- **Author**: Abhishek Gowda
- **Email**: idiot63666@gmail.com
- **GitHub**: https://github.com/The-Abhishek1

---

## 🌟 Acknowledgements

Thanks to the open-source community for inspiring this project!