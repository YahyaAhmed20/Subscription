from django.utils import timezone
from home.models import Subscriber
import requests

TELEGRAM_TOKEN = "8427273390:AAGfaz-qVBQeQ96Xghlzax2pg__NgYyA7zI"
CHAT_ID = "1028452911"

sent_today = set()  # نخزن العملاء اللي اتبعتلهم النهارده

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@shared_task
def check_monthly_payments():
    today = timezone.now().date()
    for sub in Subscriber.objects.all():
        if today >= sub.next_payment_due():
            if sub.name not in sent_today:
                message = f"💰 العميل {sub.name} المفروض يدفع النهارده ({today})"
                send_telegram_message(message)
                sent_today.add(sub.name)
