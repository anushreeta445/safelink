# SafeLink - Women Safety App 🛡️ | By The Bugsmiths

### 🚨 Problem Statement:
In an emergency, women find it difficult to unlock their phone, open an app, and type a message for help. It takes too much time and sometimes the internet is not available. This delay can be dangerous.

### 💡 Our Solution: SafeLink 2-in-1 System
We built SafeLink to send help in just ONE CLICK, with or without internet.

**1. ONLINE Mode - Secure Link Generation:**
- With one click, our Flask API generates a secure link like `safelink.in/847392`.
- This link contains the victim's live latitude and longitude.
- For privacy, the link automatically expires after 30 minutes.
- Family/Police can open the link and see the live location on Google Maps.

**2. OFFLINE Mode - No Internet Needed:**
- This is our most powerful feature. If the user has no internet, the app still works.
- It saves the location with a Google Maps link in `offline_sms_log.txt`.
- This log acts as an SMS backup. As soon as the network is available, it can be sent to emergency contacts.

### ✨ Key Features:
- One-Click SOS
- Secure & Private (Auto-expiring links)
- Works Offline
- Lightweight and Fast (Python Flask)

### 🛠️ Tech Stack:
- Backend: Python, Flask
- Location API: Google Maps API

### 👨‍💻 Team: The Bugsmiths

### ▶️ How to Run the Project:
1. Clone the repo
2. Install Flask: `pip install flask`
3. Run: `python safelink3.py`
4. Server will start at `port 5000`
