from src.image_generator import ImageGenerator


image_generator = ImageGenerator()
image_generator.generate_image("2.310", lessons=[{
        "date": "2026-05-01",
        "start_time": "0815",
        "end_time": "1130",
        "teacher": "SCJ",
        "subject": "BInf",
        "klasse": "BGT241",
        "code": 'cancelled',
        "room_changed": True,
        "anzahl": 2,
        "classroom": '2.310->2.311'
    }
])
