import pytz
from datetime import datetime, timedelta
import time


class TimeUtil():
    def __init__(self):
        self._timezone = pytz.timezone('America/Sao_Paulo')
        offset_hours = -3
        self._offset = timedelta(hours=offset_hours)



    def get_time(self):
        return self._timezone.localize(datetime.now() + self._offset).strftime('%Y-%m-%d %H:%M:%S')


    def pause(self, segundos):
        time.sleep(segundos)