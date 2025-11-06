from celery import shared_task
from django.utils import timezone
from home.models import Subscriber
import requests

TELEGRAM_TOKEN = "8427273390:AAGfaz-qVBQeQ96Xghlzax2pg__NgYyA7zI"
CHAT_ID = "1028452911"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    print("🔹 Telegram Response:", response.status_code, response.text)  # <== هنا هنطبع النتيجة

@shared_task
def check_monthly_payments():
    today = timezone.now().date()
    print("📅 Running check_monthly_payments:", today)  # <== نطبع التاريخ
    for sub in Subscriber.objects.all():
        print("👤 Checking:", sub.name, sub.next_payment_due())  # <== نطبع كل عميل
        if today >= sub.next_payment_due():
            message = f"💰 العميل {sub.name} المفروض يدفع النهارده ({today})"
            print("🚀 Sending message:", message)
            send_telegram_message(message)
