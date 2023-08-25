from _typeshed import Incomplete

from ..core import WesternCalendar

class UnitedStates(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_veterans_day: ClassVar[bool]
    veterans_day_label: ClassVar[str]
    martin_luther_king_label: ClassVar[str]
    include_thanksgiving_friday: ClassVar[bool]
    thanksgiving_friday_label: ClassVar[str]
    include_federal_presidents_day: ClassVar[bool]
    presidents_day_label: ClassVar[str]
    include_lincoln_birthday: ClassVar[bool]
    include_columbus_day: ClassVar[bool]
    columbus_day_label: ClassVar[str]
    include_confederation_day: ClassVar[bool]
    include_jefferson_davis_birthday: ClassVar[bool]
    include_cesar_chavez_day: ClassVar[bool]
    include_patriots_day: ClassVar[bool]
    boxing_day_label: ClassVar[str]
    include_election_day_every_year: ClassVar[bool]
    include_election_day_even: ClassVar[bool]
    election_day_label: ClassVar[str]
    include_inauguration_day: ClassVar[bool]
    national_memorial_day_label: ClassVar[str]
    include_fat_tuesday: ClassVar[bool]
    fat_tuesday_label: ClassVar[str]
    include_juneteenth: ClassVar[bool]
    shift_exceptions: Incomplete
    def shift(self, holidays, year): ...
    @staticmethod
    def is_presidential_year(year): ...
    def get_election_date(self, year): ...
    def get_election_day(self, year): ...
    def get_thanksgiving_friday(self, year): ...
    def get_confederate_day(self, year): ...
    def get_jefferson_davis_birthday(self, year): ...
    def get_martin_luther_king_date(self, year): ...
    def get_martin_luther_king_day(self, year): ...
    def get_presidents_day(self, year): ...
    def get_cesar_chavez_days(self, year): ...
    def get_patriots_day(self, year): ...
    def get_columbus_day(self, year): ...
    def get_lincoln_birthday(self, year): ...
    def get_inauguration_date(self, year): ...
    def get_national_memorial_day(self, year): ...
    def get_juneteenth_day(self, year): ...
    def get_variable_days(self, year): ...
    def get_veterans_day(self, year): ...
    def get_fixed_holidays(self, year): ...
    def get_calendar_holidays(self, year): ...

class FederalReserveSystem(UnitedStates):
    include_juneteenth: ClassVar[bool]
