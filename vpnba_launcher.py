import json
import os

def carica_vpnba(percorso):
    if not percorso.endswith('.vpnba'):
        raise ValueError("Il file non ha estensione .vpnba!")

    if not os.path.exists(percorso):
        raise FileNotFoundError("File .vpnba non trovato!")

    with open(percorso, 'r') as file:
        config = json.load(file)

    if config.get("type") != "vpnba-config":
        raise ValueError("Il file non è un file .vpnba valido!")

    return config

def simula_connessione(config):
    print("🔐 Avvio VPN simulata...")
    print(f"🌐 Server: {config['server']}:{config['port']} [{config['protocol']}]")
    print(f"👤 Utente: {config['user']}")
    print(f"🧪 Token: {config['token']}")
    print(f"🔄 DNS: {config['dns']}")
    if config.get("autoconnect"):
        print("✅ Connessione automatica abilitata.")
    print("🚀 VPN .vpnba ATTIVATA (simulazione).")

# Main
if __name__ == "__main__":
    try:
        percorso_file = "config.vpnba"
        config = carica_vpnba(percorso_file)
        simula_connessione(config)
    except Exception as e:
        print(f"❌ Errore: {e}")
