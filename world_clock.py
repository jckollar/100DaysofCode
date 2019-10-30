from datetime import datetime, timedelta
from pytz import timezone
import pytz


utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

est = datetime.now(pytz.timezone("US/Eastern"))
print(est)
amsterdam = datetime.now(pytz.timezone("Europe/Amsterdam"))
print(amsterdam)
fortaleza = datetime.now(pytz.timezone("America/Fortaleza"))
print(fortaleza)