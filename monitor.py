import requests
import time
from datetime import datetime

# Liste der zu überwachenden Seiten
SERVICES = [
    "https://www.google.com",
    "https://www.github.com"
]

LOG_FILE = "monitor_log.txt"

def check_uptime():
    print(f"--- Check gestartet: {datetime.now()} ---")
    
    # "a" steht für append (anhängen), damit wir nichts überschreiben
    with open(LOG_FILE, "a") as file:
        for url in SERVICES:
            try:
                response = requests.get(url, timeout=5)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if response.status_code == 200:
                    status_text = f"[{timestamp}] [UP] {url} - Status: 200\n"
                else:
                    status_text = f"[{timestamp}] [WARNING] {url} - Status: {response.status_code}\n"
                
                # In Datei schreiben UND im Terminal anzeigen
                file.write(status_text)
                print(status_text.strip())
                
            except requests.exceptions.RequestException as e:
                error_text = f"[{timestamp}] [DOWN] {url} - Error: {e}\n"
                file.write(error_text)
                print(error_text.strip())

# Das ist die Endlosschleife
if __name__ == "__main__":
    print("Monitor läuft... (Drücke Strg+C zum Stoppen)")
    try:
        while True:
            check_uptime()
            # Warte 60 Sekunden, bevor der nächste Check erfolgt
            time.sleep(60) 
    except KeyboardInterrupt:
        print("\nMonitor wurde manuell gestoppt.")