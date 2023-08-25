from _typeshed import Incomplete

from ..core import WesternCalendar

QUEENS_BIRTHDAY_EXCEPTIONS: Incomplete

from typing import ClassVar


class CaymanIslands(WesternCalendar):
    include_ash_wednesday: ClassVar[bool]
    include_good_friday: ClassVar[bool]
    include_easter_monday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    shift_new_years_day: ClassVar[bool]
    def get_variable_days(self, year): ...
    def get_national_heroes_day(self, year): ...
    def get_discovery_day(self, year): ...
    def get_queens_birthday(self, year): ...
    def get_constitution_day(self, year): ...
    def get_remembrance_day(self, year): ...
