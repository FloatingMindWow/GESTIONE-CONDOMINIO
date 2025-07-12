# GESTIONE-CONDOMINIO

Questa è una piccola applicazione Flask per la gestione dei condomini.

## Requisiti

- Python 3.12
- I pacchetti elencati in `requirements.txt`

Installa le dipendenze con:

```bash
pip install -r requirements.txt
```

## Avvio dell'applicazione

Esegui il file `app.py` per avviare il server di sviluppo:

```bash
python app.py
```

L'applicazione espone alcune API di base:

- `GET /condomini` per visualizzare l'elenco dei condomini
- `POST /condomini` per creare un nuovo condominio
- `GET /condomini/<id>` per visualizzare i dettagli di un condominio
- `POST /appartamenti` per aggiungere un appartamento a un condominio

I dati sono salvati in un database SQLite chiamato `condominio.db`.
