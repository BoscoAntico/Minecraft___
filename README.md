# VPNBA Launcher Pack

Questo pacchetto contiene un sistema personalizzato con file di configurazione custom (`.vpnba`, `.leggijava`)
e script/script launcher in HTML, Python e Java.

## 📄 File inclusi

### `index.html`
Un launcher HTML simulato. Mostra il contenuto di un file `.vpnba` e simula l'interfaccia di un launcher web.

### `config.vpnba`
File JSON con estensione personalizzata `.vpnba`, che rappresenta una configurazione VPN simulata.

### `vpnba_launcher.py`
Script Python che legge ed esegue (in modo simulato) i file `.vpnba`.

### `launcher.leggijava`
File simile a INI che contiene configurazioni per un launcher Java personalizzato.

### `LeggiJavaLauncher.java`
File Java che legge e interpreta un file `.leggijava`.

### `LeggiJavaLauncher.class`
(File compilato) della classe Java, generato con `javac`.

### `leggijava-launcher.jar`
File eseguibile `.jar` che legge file `.leggijava`.

---

## ▶️ Istruzioni rapide

### 1. Avviare il launcher HTML
Apri `index.html` in un browser. Simula il caricamento della config `.vpnba`.

### 2. Eseguire la VPN in Python
```bash
python3 vpnba_launcher.py
```

### 3. Compilare il programma Java
```bash
javac LeggiJavaLauncher.java
java LeggiJavaLauncher
```

### 4. Creare un JAR
```bash
jar cfe leggijava-launcher.jar LeggiJavaLauncher LeggiJavaLauncher.class
```

---

Creato con ❤️ da ChatGPT.
