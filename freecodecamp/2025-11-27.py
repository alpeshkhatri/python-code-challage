from datetime import datetime, timedelta
def calculate_age(birthday):
    return int((datetime.fromisoformat('2025-11-27') - datetime.fromisoformat(birthday)).days//365.25)
