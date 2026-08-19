
import serial
import time
from twilio.rest import Client

# ---------------- TWILIO ----------------
account_sid = 'ACb0d1c3d2755188936d961f41bb94044b'
auth_token = 'ba7765a2a24365374a3d530dedb83f06'
twilio_number = '+16624433975'   # your Twilio number

client = Client(account_sid, auth_token)

# ---------------- SERIAL ----------------
ser = serial.Serial('COM6', 115200, timeout=1)   # change COM port if needed
time.sleep(2)

# ---------------- CONTACTS ----------------
numbers = [
       "+917358072276",
    "+919495010168",
    "+917358268215"
]

# ---------------- FIXED LOCATION ----------------
fixed_location = "https://maps.app.goo.gl/kpyVvJ8FH8bsvehs5?g_st=ac"

last_sms_time = 0
cooldown_seconds = 20

def send_sms():
    global last_sms_time

    now = time.time()
    if now - last_sms_time < cooldown_seconds:
        print("SMS cooldown active. Not sending again yet.")
        return

    body = f"🚨 Accident Detected!\nHelp needed!\nLocation: {fixed_location}"

    for num in numbers:
        try:
            client.messages.create(
                body=body,
                from_=twilio_number,
                to=num
            )
            print(f"Sent to {num}")
        except Exception as e:
            print(f"Failed for {num}: {e}")

    last_sms_time = now

print("Waiting for ESP32...")

while True:
    try:
        data = ser.readline().decode(errors="ignore").strip()
        if not data:
            continue

        print("Received:", data)

        if data == "CANCELLED":
            print("Alert cancelled. No SMS sent.")

        elif data.startswith("ACCIDENT"):
            print("Sending SMS...")
            send_sms()

    except Exception as e:
        print("Error:", e)