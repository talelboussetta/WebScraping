import time
import smtplib
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
#THIS PROGRAM ALLOWS YOU TO SEARCH A WEBSITE AND SENDS YOU A NOTIFICATION WHEN THERE IS CHANGES
# Website URL
URL = "https://your__website.com/appointment_page"

# Email Settings (For Notifications)
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"
TO_EMAIL = "your_email@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Start Chrome in Undetected Mode
options = uc.ChromeOptions()
options.headless = True  # Run without opening a window
driver = uc.Chrome(options=options)


def send_email_notification():
    """Sends an email when an update is detected."""
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        subject = "Enter your subject here!"
        body = f"Enter a message you want to get here! Visit: {URL}"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL, TO_EMAIL, message)
        server.quit()
        print("📧 Email notification sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)


def get_page_content():
    """Fetches and parses the website content."""
    driver.get(URL)
    time.sleep(5)  # Wait for page to fully load
    return BeautifulSoup(driver.page_source, "html.parser").text  # Extract text content


# Store initial page content
previous_content = get_page_content()
print("🔍 Monitoring your designed website...")

while True:
    time.sleep(30)  # Wait before checking again (adjust as needed)

    current_content = get_page_content()
    if current_content != previous_content:
        print("⚠️ Website updated! Sending notification...")
        send_email_notification()
        previous_content = current_content  # Update stored content
    else:
        print("✅ No changes detected, checking again...")
