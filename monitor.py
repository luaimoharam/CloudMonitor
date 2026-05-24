import requests
from datetime import datetime

# Die 5 wichtigsten Streaming-Dienste
SERVICES = [
    "https://www.netflix.com",
    "https://www.disneyplus.com",
    "https://www.primevideo.com",
    "https://www.spotify.com",
    "https://www.youtube.com"
]

def check_streaming_services():
    print(f"--- Streaming-Status Check: {datetime.now().strftime('%H:%M:%S')} ---")
    
    for url in SERVICES:
        try:
            # Wir setzen einen "User-Agent", damit wir nicht sofort wie ein Bot blockiert werden
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"[OK]   {url}")
            else:
                # Bei Streaming-Seiten ist ein 403 oft normal (Sicherheits-Schutz)
                print(f"[WARN] {url} - Status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"[DOWN] {url} - Fehler: Verbindung fehlgeschlagen")

    print("--- Check abgeschlossen ---")

if __name__ == "__main__":
    check_streaming_services()