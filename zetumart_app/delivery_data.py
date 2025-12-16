"""
Kenya Counties, Cities/Towns, and Delivery Data
Dynamic delivery system data structure for ZetuMart
"""

DELIVERY_DATA = {
    "nairobi": {
        "name": "Nairobi",
        "major_city": True,
        "delivery_fee": 150,
        "estimated_days": "1-2",
        "cities": [
            {"name": "Nairobi Central", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Westlands", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Kilimani", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Kileleshwa", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Lavington", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Karen", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Langata", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Runda", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Muthaiga", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Parklands", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Eastlands", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Embakasi", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Kasarani", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Dagoretti", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Roysambu", "delivery_fee": 200, "estimated_days": "1-2"}
        ]
    },
    "mombasa": {
        "name": "Mombasa",
        "major_city": True,
        "delivery_fee": 250,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Mombasa Island", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Nyali", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Bamburi", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Kisauni", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Likoni", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Changamwe", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Jomvu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Miritini", "delivery_fee": 350, "estimated_days": "3"}
        ]
    },
    "kisumu": {
        "name": "Kisumu",
        "major_city": True,
        "delivery_fee": 300,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Kisumu Central", "delivery_fee": 300, "estimated_days": "2"},
            {"name": "Milimani", "delivery_fee": 300, "estimated_days": "2"},
            {"name": "Nyalenda", "delivery_fee": 350, "estimated_days": "2-3"},
            {"name": "Manyatta", "delivery_fee": 350, "estimated_days": "2-3"},
            {"name": "Kondele", "delivery_fee": 350, "estimated_days": "2-3"},
            {"name": "Obunga", "delivery_fee": 350, "estimated_days": "2-3"}
        ]
    },
    "nakuru": {
        "name": "Nakuru",
        "major_city": True,
        "delivery_fee": 250,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Nakuru Town", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "London Estate", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Kabarak", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Nakuru West", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Bahati", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Njoro", "delivery_fee": 400, "estimated_days": "3-4"}
        ]
    },
    "eldoret": {
        "name": "Eldoret",
        "major_city": True,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Eldoret Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Kapsoya", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Elgeyo", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kapsowar", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Iten", "delivery_fee": 450, "estimated_days": "4"}
        ]
    },
    "thika": {
        "name": "Thika",
        "major_city": False,
        "delivery_fee": 200,
        "estimated_days": "1-2",
        "cities": [
            {"name": "Thika Town", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Makongeni", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Kilimambogo", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Gatanga", "delivery_fee": 300, "estimated_days": "2-3"}
        ]
    },
    "kitui": {
        "name": "Kitui",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kitui Town", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Mutomo", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mwingi", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Ikutha", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "machakos": {
        "name": "Machakos",
        "major_city": False,
        "delivery_fee": 250,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Machakos Town", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Athi River", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Mavoko", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Kangundo", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Tala", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Matuu", "delivery_fee": 350, "estimated_days": "3"}
        ]
    },
    "kajiado": {
        "name": "Kajiado",
        "major_city": False,
        "delivery_fee": 300,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Kajiado Town", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Ngong", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Ongata Rongai", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Kiserian", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Isinya", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Namanga", "delivery_fee": 400, "estimated_days": "3-4"}
        ]
    },
    "nyandarua": {
        "name": "Nyandarua",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Ol Kalou", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Nyahururu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Ndaragwa", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Ol Joro Orok", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kinangop", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "nyeri": {
        "name": "Nyeri",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Nyeri Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Othaya", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Mukurweini", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Karatina", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Tetu", "delivery_fee": 450, "estimated_days": "4"}
        ]
    },
    "kirinyaga": {
        "name": "Kirinyaga",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kerugoya", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Kutus", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Sagana", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Kianyaga", "delivery_fee": 400, "estimated_days": "4"},
            {"name": "Baricho", "delivery_fee": 400, "estimated_days": "4"}
        ]
    },
    "muranga": {
        "name": "Murang'a",
        "major_city": False,
        "delivery_fee": 300,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Murang'a Town", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Kangema", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Kiharu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Kigumo", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Gatanga", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Mathioya", "delivery_fee": 400, "estimated_days": "3-4"}
        ]
    },
    "kiambu": {
        "name": "Kiambu",
        "major_city": False,
        "delivery_fee": 200,
        "estimated_days": "1-2",
        "cities": [
            {"name": "Kiambu Town", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Thika", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Limuru", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Kikuyu", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Ruiru", "delivery_fee": 150, "estimated_days": "1"},
            {"name": "Juja", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Githunguri", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Lari", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Gatundu", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Ndarugu", "delivery_fee": 300, "estimated_days": "2-3"}
        ]
    },
    "turkana": {
        "name": "Turkana",
        "major_city": False,
        "delivery_fee": 800,
        "estimated_days": "5-7",
        "cities": [
            {"name": "Lodwar", "delivery_fee": 800, "estimated_days": "5"},
            {"name": "Kakuma", "delivery_fee": 850, "estimated_days": "5-7"},
            {"name": "Lokichoggio", "delivery_fee": 900, "estimated_days": "6-7"},
            {"name": "Lokichar", "delivery_fee": 900, "estimated_days": "6-7"}
        ]
    },
    "west_pokot": {
        "name": "West Pokot",
        "major_city": False,
        "delivery_fee": 700,
        "estimated_days": "5-7",
        "cities": [
            {"name": "Kapenguria", "delivery_fee": 700, "estimated_days": "5"},
            {"name": "Makutano", "delivery_fee": 750, "estimated_days": "5-6"},
            {"name": "Chepareria", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Sigor", "delivery_fee": 800, "estimated_days": "6"}
        ]
    },
    "samburu": {
        "name": "Samburu",
        "major_city": False,
        "delivery_fee": 750,
        "estimated_days": "5-7",
        "cities": [
            {"name": "Maralal", "delivery_fee": 750, "estimated_days": "5"},
            {"name": "Baragoi", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Archers Post", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Wamba", "delivery_fee": 800, "estimated_days": "6"}
        ]
    },
    "trans_nzoia": {
        "name": "Trans Nzoia",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kitale", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Endebess", "delivery_fee": 450, "estimated_days": "3-4"},
            {"name": "Saboti", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kwanza", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Cherangany", "delivery_fee": 500, "estimated_days": "4"}
        ]
    },
    "uasin_gishu": {
        "name": "Uasin Gishu",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Eldoret", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Moiben", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Burnt Forest", "delivery_fee": 400, "estimated_days": "4"},
            {"name": "Tinderet", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kesses", "delivery_fee": 400, "estimated_days": "3-4"}
        ]
    },
    "elgeyo_marakwet": {
        "name": "Elgeyo Marakwet",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Iten", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kapsowar", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Chebiemit", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Kapkateny", "delivery_fee": 500, "estimated_days": "5"},
            {"name": "Embobut", "delivery_fee": 550, "estimated_days": "5"}
        ]
    },
    "nandi": {
        "name": "Nandi",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kapsabet", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Nandi Hills", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kobujoi", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Chepterwai", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Kabiyet", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "baringo": {
        "name": "Baringo",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Kabarnet", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Mogotio", "delivery_fee": 450, "estimated_days": "3-4"},
            {"name": "Eldama Ravine", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Marigat", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Tenges", "delivery_fee": 600, "estimated_days": "5"}
        ]
    },
    "laikipia": {
        "name": "Laikipia",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Nanyuki", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Nyahururu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Rumuruti", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Dol Dol", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Ol Jabet", "delivery_fee": 550, "estimated_days": "5"}
        ]
    },
    "nakuru": {
        "name": "Nakuru",
        "major_city": True,
        "delivery_fee": 250,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Nakuru Town", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Naivasha", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Gilgil", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Molo", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Njoro", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Rongai", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Subukia", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Bahati", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Elementaita", "delivery_fee": 350, "estimated_days": "3"}
        ]
    },
    "bomet": {
        "name": "Bomet",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Bomet Town", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Silibwet", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Konoin", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Chepalungu", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Tinderet", "delivery_fee": 450, "estimated_days": "4"}
        ]
    },
    "kericho": {
        "name": "Kericho",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kericho Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Litein", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kapsoit", "delivery_fee": 400, "estimated_days": "4"},
            {"name": "Kipkelion", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Cheptongei", "delivery_fee": 450, "estimated_days": "4"}
        ]
    },
    "kisii": {
        "name": "Kisii",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kisii Town", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Ogembo", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Nyamache", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Keroka", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Igangara", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "nyamira": {
        "name": "Nyamira",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Nyamira Town", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Rigoma", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Manga", "delivery_fee": 500, "estimated_days": "5"},
            {"name": "Ekerenyo", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Nyansiongo", "delivery_fee": 550, "estimated_days": "5"}
        ]
    },
    "migori": {
        "name": "Migori",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Migori Town", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Awendo", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Rongo", "delivery_fee": 500, "estimated_days": "5"},
            {"name": "Kehancha", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Suna", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Isebania", "delivery_fee": 600, "estimated_days": "5-6"}
        ]
    },
    "homa_bay": {
        "name": "Homa Bay",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Homa Bay Town", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Mbita", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Oyugis", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Kendu Bay", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Rachuonyo", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Ndhiwa", "delivery_fee": 600, "estimated_days": "5-6"}
        ]
    },
    "siaya": {
        "name": "Siaya",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Siaya Town", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Bondo", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Ugenya", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Yimbo", "delivery_fee": 600, "estimated_days": "5-6"},
            {"name": "Ugunja", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Gem", "delivery_fee": 600, "estimated_days": "5-6"}
        ]
    },
    "busia": {
        "name": "Busia",
        "major_city": False,
        "delivery_fee": 550,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Busia Town", "delivery_fee": 550, "estimated_days": "4"},
            {"name": "Nambale", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Butula", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Funyula", "delivery_fee": 650, "estimated_days": "5-6"},
            {"name": "Teso South", "delivery_fee": 650, "estimated_days": "5-6"},
            {"name": "Teso North", "delivery_fee": 650, "estimated_days": "5-6"}
        ]
    },
    "kakamega": {
        "name": "Kakamega",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kakamega Town", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Lugari", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Malava", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Shinyalu", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Ikolomani", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Shirere", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mumias", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Butere", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Matungu", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Navakholo", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Khwisero", "delivery_fee": 550, "estimated_days": "5"}
        ]
    },
    "vihiga": {
        "name": "Vihiga",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Mbale", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Vihiga Town", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Sabatia", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Hamisi", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Luanda", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Emuhaya", "delivery_fee": 550, "estimated_days": "5"}
        ]
    },
    "bungoma": {
        "name": "Bungoma",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Bungoma Town", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Webuye", "delivery_fee": 450, "estimated_days": "3-4"},
            {"name": "Kimilili", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Tongaren", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Kanduyi", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Sirisia", "delivery_fee": 600, "estimated_days": "5-6"},
            {"name": "Cheptais", "delivery_fee": 600, "estimated_days": "5-6"},
            {"name": "Mt Elgon", "delivery_fee": 650, "estimated_days": "6"}
        ]
    },
    "trans_nzoia": {
        "name": "Trans Nzoia",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kitale", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Endebess", "delivery_fee": 450, "estimated_days": "3-4"},
            {"name": "Saboti", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kwanza", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Cherangany", "delivery_fee": 500, "estimated_days": "4"}
        ]
    },
    "garissa": {
        "name": "Garissa",
        "major_city": True,
        "delivery_fee": 600,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Garissa Town", "delivery_fee": 600, "estimated_days": "4"},
            {"name": "Balambala", "delivery_fee": 650, "estimated_days": "5"},
            {"name": "Dadaab", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Ijara", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Lagdera", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Fafi", "delivery_fee": 750, "estimated_days": "6"}
        ]
    },
    "wajir": {
        "name": "Wajir",
        "major_city": False,
        "delivery_fee": 700,
        "estimated_days": "5-6",
        "cities": [
            {"name": "Wajir Town", "delivery_fee": 700, "estimated_days": "5"},
            {"name": "Buna", "delivery_fee": 750, "estimated_days": "5-6"},
            {"name": "Habaswein", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Tarbaj", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Wajir Bor", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Eldas", "delivery_fee": 750, "estimated_days": "6"}
        ]
    },
    "mandera": {
        "name": "Mandera",
        "major_city": False,
        "delivery_fee": 800,
        "estimated_days": "6-7",
        "cities": [
            {"name": "Mandera Town", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Elwak", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Rhamu", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Banisa", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Takaba", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Kutulo", "delivery_fee": 900, "estimated_days": "7"}
        ]
    },
    "marsabit": {
        "name": "Marsabit",
        "major_city": False,
        "delivery_fee": 750,
        "estimated_days": "5-7",
        "cities": [
            {"name": "Marsabit Town", "delivery_fee": 750, "estimated_days": "5"},
            {"name": "Moyale", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "North Horr", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Laisamis", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Sololo", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Loiyangalani", "delivery_fee": 950, "estimated_days": "7"}
        ]
    },
    "isiolo": {
        "name": "Isiolo",
        "major_city": False,
        "delivery_fee": 600,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Isiolo Town", "delivery_fee": 600, "estimated_days": "4"},
            {"name": "Merti", "delivery_fee": 650, "estimated_days": "5"},
            {"name": "Garba Tula", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Kina", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Oldonyiro", "delivery_fee": 750, "estimated_days": "6"}
        ]
    },
    "meru": {
        "name": "Meru",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Meru Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Nkubu", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Maua", "delivery_fee": 400, "estimated_days": "4"},
            {"name": "Timau", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kianjai", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Imenti North", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Imenti South", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Tigania East", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Tigania West", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Buuri", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "tharaka_nithi": {
        "name": "Tharaka Nithi",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Kathwana", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Chuka", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Marimanti", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Nkondi", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Tharaka", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Igamba Ng'ombe", "delivery_fee": 500, "estimated_days": "5"}
        ]
    },
    "embu": {
        "name": "Embu",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Embu Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Runyenjes", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Manyatta", "delivery_fee": 400, "estimated_days": "4"},
            {"name": "Mbeere South", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mbeere North", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kirinyaga", "delivery_fee": 350, "estimated_days": "3-4"}
        ]
    },
    "kitui": {
        "name": "Kitui",
        "major_city": False,
        "delivery_fee": 400,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kitui Town", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Mwingi", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mutomo", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Ikutha", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Tseikuru", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Kyuso", "delivery_fee": 550, "estimated_days": "5"},
            {"name": "Mwingi Central", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mwingi North", "delivery_fee": 500, "estimated_days": "4-5"},
            {"name": "Mwingi West", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "makueni": {
        "name": "Makueni",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Wote", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Makindu", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kibwezi", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mtito Andei", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kathonzweni", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Mbooni", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kilungu", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Nzaui", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Kaiti", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Chyulu", "delivery_fee": 500, "estimated_days": "4-5"}
        ]
    },
    "machakos": {
        "name": "Machakos",
        "major_city": False,
        "delivery_fee": 250,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Machakos Town", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Athi River", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Mavoko", "delivery_fee": 200, "estimated_days": "1-2"},
            {"name": "Kangundo", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Tala", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Matuu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Masinga", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Yatta", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Kathekakai", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Mwala", "delivery_fee": 350, "estimated_days": "3"}
        ]
    },
    "kwale": {
        "name": "Kwale",
        "major_city": False,
        "delivery_fee": 350,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Kwale Town", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Ukunda", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Diani", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Msambweni", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Shimoni", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Lungalunga", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kinango", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Samburu", "delivery_fee": 450, "estimated_days": "4"},
            {"name": "Vanga", "delivery_fee": 450, "estimated_days": "4"}
        ]
    },
    "kilifi": {
        "name": "Kilifi",
        "major_city": False,
        "delivery_fee": 300,
        "estimated_days": "2-3",
        "cities": [
            {"name": "Kilifi Town", "delivery_fee": 300, "estimated_days": "2"},
            {"name": "Malindi", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Watamu", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Mtwapa", "delivery_fee": 250, "estimated_days": "2"},
            {"name": "Mariakani", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Ganze", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Bamba", "delivery_fee": 400, "estimated_days": "3-4"},
            {"name": "Kaloleni", "delivery_fee": 300, "estimated_days": "2-3"},
            {"name": "Magarini", "delivery_fee": 350, "estimated_days": "3"},
            {"name": "Changamwe", "delivery_fee": 300, "estimated_days": "2-3"}
        ]
    },
    "tana_river": {
        "name": "Tana River",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Hola", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Garissa", "delivery_fee": 600, "estimated_days": "4-5"},
            {"name": "Madogo", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Garsen", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Kipini", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Witu", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Bangale", "delivery_fee": 650, "estimated_days": "5-6"}
        ]
    },
    "lamu": {
        "name": "Lamu",
        "major_city": False,
        "delivery_fee": 600,
        "estimated_days": "5-7",
        "cities": [
            {"name": "Lamu Town", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Mpeketoni", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Hindi", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Manda", "delivery_fee": 650, "estimated_days": "5-6"},
            {"name": "Pate", "delivery_fee": 700, "estimated_days": "6"},
            {"name": "Faza", "delivery_fee": 700, "estimated_days": "6"},
            {"name": "Kiunga", "delivery_fee": 750, "estimated_days": "6-7"}
        ]
    },
    "taita_taveta": {
        "name": "Taita Taveta",
        "major_city": False,
        "delivery_fee": 450,
        "estimated_days": "3-4",
        "cities": [
            {"name": "Wundanyi", "delivery_fee": 450, "estimated_days": "3"},
            {"name": "Mwatate", "delivery_fee": 450, "estimated_days": "3"},
            {"name": "Taveta", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Voi", "delivery_fee": 400, "estimated_days": "3"},
            {"name": "Mbololo", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Bomani", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Chala", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Mgange", "delivery_fee": 550, "estimated_days": "4-5"}
        ]
    },
    "tana_river": {
        "name": "Tana River",
        "major_city": False,
        "delivery_fee": 500,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Hola", "delivery_fee": 500, "estimated_days": "4"},
            {"name": "Madogo", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Garsen", "delivery_fee": 550, "estimated_days": "4-5"},
            {"name": "Kipini", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Witu", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Bangale", "delivery_fee": 650, "estimated_days": "5-6"},
            {"name": "Bura", "delivery_fee": 600, "estimated_days": "5"},
            {"name": "Galole", "delivery_fee": 650, "estimated_days": "5-6"}
        ]
    },
    "garissa": {
        "name": "Garissa",
        "major_city": True,
        "delivery_fee": 600,
        "estimated_days": "4-5",
        "cities": [
            {"name": "Garissa Town", "delivery_fee": 600, "estimated_days": "4"},
            {"name": "Balambala", "delivery_fee": 650, "estimated_days": "5"},
            {"name": "Dadaab", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Ijara", "delivery_fee": 700, "estimated_days": "5-6"},
            {"name": "Lagdera", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Fafi", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Liboi", "delivery_fee": 800, "estimated_days": "6-7"},
            {"name": "Masalani", "delivery_fee": 700, "estimated_days": "5-6"}
        ]
    },
    "wajir": {
        "name": "Wajir",
        "major_city": False,
        "delivery_fee": 700,
        "estimated_days": "5-6",
        "cities": [
            {"name": "Wajir Town", "delivery_fee": 700, "estimated_days": "5"},
            {"name": "Buna", "delivery_fee": 750, "estimated_days": "5-6"},
            {"name": "Habaswein", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Tarbaj", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Wajir Bor", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Eldas", "delivery_fee": 750, "estimated_days": "6"},
            {"name": "Qara", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Griftu", "delivery_fee": 850, "estimated_days": "6-7"}
        ]
    },
    "mandera": {
        "name": "Mandera",
        "major_city": False,
        "delivery_fee": 800,
        "estimated_days": "6-7",
        "cities": [
            {"name": "Mandera Town", "delivery_fee": 800, "estimated_days": "6"},
            {"name": "Elwak", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Rhamu", "delivery_fee": 850, "estimated_days": "6-7"},
            {"name": "Banisa", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Takaba", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Kutulo", "delivery_fee": 900, "estimated_days": "7"},
            {"name": "Lafey", "delivery_fee": 950, "estimated_days": "7"},
            {"name": "Ashabito", "delivery_fee": 950, "estimated_days": "7"}
        ]
    }
}

# Delivery methods and their descriptions
DELIVERY_METHODS = {
    "home": {
        "name": "Home Delivery",
        "description": "Delivered to your home address",
        "icon": "bi-house-door",
        "time_options": [
            {"value": "anytime", "label": "Anytime", "description": "Delivery anytime during business hours"},
            {"value": "morning", "label": "Morning (8AM-12PM)", "description": "Delivery between 8AM and 12PM"},
            {"value": "afternoon", "label": "Afternoon (12PM-5PM)", "description": "Delivery between 12PM and 5PM"},
            {"value": "evening", "label": "Evening (5PM-8PM)", "description": "Delivery between 5PM and 8PM"}
        ]
    },
    "office": {
        "name": "Office Delivery",
        "description": "Delivered to your office/workplace",
        "icon": "bi-building",
        "time_options": [
            {"value": "morning", "label": "Morning (8AM-12PM)", "description": "Delivery between 8AM and 12PM"},
            {"value": "afternoon", "label": "Afternoon (12PM-5PM)", "description": "Delivery between 12PM and 5PM"}
        ]
    },
    "pickup": {
        "name": "Pickup Station",
        "description": "Collect from our pickup station",
        "icon": "bi-shop",
        "time_options": [
            {"value": "morning", "label": "Morning (8AM-12PM)", "description": "Pickup between 8AM and 12PM"},
            {"value": "afternoon", "label": "Afternoon (12PM-5PM)", "description": "Pickup between 12PM and 5PM"}
        ]
    }
}

# Helper functions
def get_county_list():
    """Get list of all counties with search-friendly format"""
    counties = []
    for key, data in DELIVERY_DATA.items():
        counties.append({
            'key': key,
            'name': data['name'],
            'major_city': data.get('major_city', False),
            'delivery_fee': data['delivery_fee'],
            'estimated_days': data['estimated_days']
        })
    return sorted(counties, key=lambda x: (not x['major_city'], x['name']))

def search_counties(query):
    """Search counties by name"""
    query = query.lower().strip()
    if not query:
        return get_county_list()[:10]  # Return first 10 if no query
    
    results = []
    for county in get_county_list():
        if query in county['name'].lower():
            results.append(county)
    
    return results

def get_cities_for_county(county_key):
    """Get cities/towns for a specific county"""
    if county_key not in DELIVERY_DATA:
        return []
    
    return DELIVERY_DATA[county_key]['cities']

def search_cities(county_key, query):
    """Search cities within a county"""
    query = query.lower().strip()
    cities = get_cities_for_county(county_key)
    
    if not query:
        return cities[:10]  # Return first 10 if no query
    
    results = []
    for city in cities:
        if query in city['name'].lower():
            results.append(city)
    
    return results

def get_delivery_info(county_key, city_name):
    """Get delivery information for specific county and city"""
    if county_key not in DELIVERY_DATA:
        return None
    
    county_data = DELIVERY_DATA[county_key]
    
    # Find city data
    city_data = None
    for city in county_data['cities']:
        if city['name'].lower() == city_name.lower():
            city_data = city
            break
    
    if not city_data:
        return None
    
    return {
        'county': county_data['name'],
        'county_key': county_key,
        'city': city_data['name'],
        'delivery_fee': city_data['delivery_fee'],
        'estimated_days': city_data['estimated_days'],
        'is_major_city': county_data.get('major_city', False)
    }

def calculate_delivery_fee(county_key, city_name, order_amount=0):
    """Calculate delivery fee with possible discounts"""
    info = get_delivery_info(county_key, city_name)
    if not info:
        return 0
    
    base_fee = info['delivery_fee']
    
    # Free delivery for orders above threshold
    if order_amount >= 5000:  # Free delivery for orders above KSh 5000
        return 0
    
    # Discount for major cities
    if info['is_major_city'] and order_amount >= 2000:
        base_fee = max(base_fee - 50, 100)  # Minimum KSh 100
    
    return base_fee

def get_estimated_delivery_date(county_key, city_name, days_ahead=0):
    """Calculate estimated delivery date"""
    info = get_delivery_info(county_key, city_name)
    if not info:
        return None
    
    from datetime import datetime, timedelta
    
    # Parse estimated days
    days_range = info['estimated_days'].split('-')
    if len(days_range) == 2:
        min_days = int(days_range[0])
        max_days = int(days_range[1])
    else:
        min_days = max_days = int(days_range[0])
    
    # Add business days only
    current_date = datetime.now()
    delivery_days = 0
    
    while delivery_days < min_days:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Monday to Friday
            delivery_days += 1
    
    estimated_date = current_date
    
    return {
        'min_date': estimated_date.strftime('%Y-%m-%d'),
        'max_date': (estimated_date + timedelta(days=max_days - min_days)).strftime('%Y-%m-%d'),
        'formatted_date': estimated_date.strftime('%A, %B %d, %Y'),
        'days_range': info['estimated_days']
    }
