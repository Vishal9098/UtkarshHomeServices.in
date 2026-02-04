import requests
from django.conf import settings


def send_whatsapp_message(order):
    # ✅ phone yaha define hota hai
    phone = order.customer.mobile

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
            "name": "hello_world",   # ✅ approved template
            "language": {
                "code": "en_US"
            }
        }
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=20
    )

    print("WHATSAPP STATUS:", response.status_code)
    print("WHATSAPP RESPONSE:", response.text)

    return response.json()

# alias (same function, different name)
send_whatsapp_english = send_whatsapp_message
