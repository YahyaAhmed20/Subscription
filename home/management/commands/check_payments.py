from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import Subscriber
import requests

# 🔹 بيانات البوت
TELEGRAM_TOKEN = "8427273390:AAGfaz-qVBQeQ96Xghlzax2pg__NgYyA7zI"
CHAT_ID = "1028452911"

def send_telegram_message(text):
    """يبعت رسالة لتليجرام"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print("Telegram Error:", e)

class Command(BaseCommand):
    help = 'Check monthly payments and notify if due'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        subscribers = Subscriber.objects.all()

        for sub in subscribers:
            if today >= sub.next_payment_due():
                message = (
                    f"💰 العميل {sub.name} المفروض يدفع النهارده ({today})"
                )
                send_telegram_message(message)
                self.stdout.write(self.style.SUCCESS(f"تم إرسال إشعار لـ {sub.name}"))
