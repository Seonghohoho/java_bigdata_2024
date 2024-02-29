#file : p43_thread.py
#desc: 스레드 기본

from threading import Thread, current_thread
import time
from typing import Iterable, Mapping

class BackgroundWorker(Thread):
    def __init__(self, name) -> None:
        super().__init__(name=name)
        self._name = f'{current_thread().getName()}:{name}'

        