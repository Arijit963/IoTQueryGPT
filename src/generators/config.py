# ==========================================================
# Output
# ==========================================================

OUTPUT_FILE = "data/iot_queries.txt"

# ==========================================================
# Numeric Fields
# ==========================================================

NUMERIC_FIELDS = {
    "temperature": {
        "table": "sensors",
        "min": 10,
        "max": 80,
        "step": 1,
        "unit": "degrees"
    },

    "humidity": {
        "table": "sensors",
        "min": 20,
        "max": 90,
        "step": 1,
        "unit": "percent"
    },

    "pressure": {
        "table": "sensors",
        "min": 980,
        "max": 1050,
        "step": 10,
        "unit": ""
    },

    "battery": {
        "table": "devices",
        "min": 10,
        "max": 100,
        "step": 5,
        "unit": "percent"
    }
}

# ==========================================================
# Rooms
# ==========================================================

ROOMS = [
    "A",
    "B",
    "C",
    "Lab 1",
    "Lab 2",
    "Warehouse"
]

# ==========================================================
# Device Status
# ==========================================================

STATUS = [
    "active",
    "inactive",
    "online",
    "offline",
    "maintenance"
]

# ==========================================================
# Locations
# ==========================================================

LOCATIONS = [
    "Warehouse",
    "Factory",
    "Building A",
    "Building B",
    "Floor 1",
    "Floor 2",
    "Floor 3",
    "Server Room",
    "Control Room"
]