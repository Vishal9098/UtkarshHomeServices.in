# utils.py
import requests
from django.conf import settings
# from .utils import send_whatsapp_english

def send_whatsapp_message(order):
    phone = order.customer.mobile.strip()

    # 📞 Proper E.164 format
    if phone.startswith("+"):
        phone = phone.replace("+", "")
    if not phone.startswith("91"):
        phone = "91" + phone

    url = f"https://graph.facebook.com/v19.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            # 🔥 EXACT TEMPLATE NAME
            "name": "booking_accepted",
            "language": {"code": "hi"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": order.customer.name
                        },
                        {
                            "type": "text",
                            "text": order.product.title
                        },
                        {
                            "type": "text",
                            "text": str(order.price)
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, json=payload, headers=headers, timeout=20)

    print("WHATSAPP STATUS:", response.status_code)
    print("WHATSAPP RESPONSE:", response.text)

    return response.json()
