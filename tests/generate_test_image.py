from src.image_generator import ImageGenerator


image_generator = ImageGenerator()
image_generator.generate_image("2.310", lessons=[{
        "start": "0815",
        "end": "1130",
        "teacher": "SCJ",
        "subject": "BInf",
        "class": "BGT241",
        "changed": False,
        "is_double": True,
    },
    {
        "start": "1145",
        "end": "1315",
        "teacher": "SID",
        "subject": "IFT",
        "class": "BGT241",
        "changed": False,
        "is_double": False,
    }, {
        "start": "1345",
        "end": "1615",
        "teacher": "WIB",
        "subject": "DEU",
        "class": "BGT241",
        "changed": False,
        "is_double": True,
    }
])
