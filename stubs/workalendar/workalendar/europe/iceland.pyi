from _typeshed import Incomplete
from typing import ClassVar

from ..core import WesternCalendar


class Iceland(WesternCalendar):
    include_holy_thursday: ClassVar[bool]
    include_good_friday: ClassVar[bool]
    include_easter_monday: ClassVar[bool]
    include_ascension: ClassVar[bool]
    include_whit_monday: ClassVar[bool]
    include_christmas_eve: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    boxing_day_label: ClassVar[str]
    include_labour_day: ClassVar[bool]
    FIXED_HOLIDAYS: Incomplete
    def get_first_day_of_summer(self, year): ...
    def get_commerce_day(self, year): ...
    def get_variable_days(self, year): ...
