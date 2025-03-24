# **Website Change Notifier** 🚀  

A Python script that monitors a **specific webpage** for updates and **sends a notification** when a change is detected. Useful for tracking appointment availability, product restocks, or any important updates on a website.  

## **Features**  
✅ **Automatic Page Monitoring** – Periodically checks for content changes.  
✅ **Stealth Mode** – Mimics real user behavior to avoid detection.  
✅ **Email Notifications** – Sends an alert when an update is found.  
✅ **Easy to Customize** – Modify the URL, check frequency, and notification method.  

## **Installation**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/website-change-notifier.git
   cd website-change-notifier
   ```  

2. **Install dependencies**  
   ```bash
   pip install selenium requests beautifulsoup4 undetected-chromedriver
   ```  

3. **Set up your environment**  
   - Download **Chrome WebDriver** ([here](https://chromedriver.chromium.org/downloads))  
   - Update the script with your **target website URL**  
   - Configure **email settings** for notifications  

## **Usage**  

Run the script with:  
```bash
python monitor.py
```  
It will keep checking the page and notify you when an update is detected.  

## **Customization**  
- Change the `URL` variable in `monitor.py` to your target webpage.  
- Adjust the `time.sleep()` interval for how often it checks.  
- Modify the notification method (e.g., Telegram, SMS, Discord Webhook).  

## **Disclaimer**  
Use this script **ethically and responsibly**. Ensure that **automated monitoring** is allowed on the target website before using this tool.  

---
