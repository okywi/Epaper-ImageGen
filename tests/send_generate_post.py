import requests


result = requests.post('http://127.0.0.1:8080/generate', json={
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
]})

print(result.text)