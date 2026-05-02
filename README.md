# Epaper-ImageGen
Generates the e paper images.

## Running with docker
```commandline
chmod +x ./run.sh
./run.sh
```

## Endpoints
### Get /health
Gibt den aktuellen Status des Microservices zurück

### Get /image
Gibt das Image für einen Raum zurück

**Para**

|Name|Typ| Beschreibung             |
|-----|----|--------------------------|
|room|str| Name des Raums z.B. 2.310|

GET /image?room=2.310

**Response 400** – Room nicht angegeben
```json
{ "status": "yellow", "error": "room was not provided." }
```

**Response 404** – Image wurde nicht gefunden
```json
{
  "status": "red",
  "error": "The file does not exist. Did you spell the room correctly?'"
}

```


### Post /generate
Generiert das Bild anhand der mitgelieferten Daten

Format:
```json
{
    "room": "2.310",
    "lessons":[{
        "date": "2026-05-01",
        "start_time": "0815",
        "end_time": "1130",
        "teacher": "SCJ",
        "subject": "BInf",
        "klasse": "BGT241",
        "code": 'cancelled',
        "room_changed": True,
        "anzahl": 4,
        "classroom": '2.310->2.311'
    },{
        "date": "2026-05-01",
        "start_time": "1145",
        "end_time": "1315",
        "teacher": "SID",
        "subject": "IFT",
        "klasse": "BGT241",
        "code": '',
        "room_changed": False,
        "anzahl": 2,
        "classroom": '2.311'
    }
]}
```
