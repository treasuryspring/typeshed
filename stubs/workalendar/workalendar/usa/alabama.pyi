from .core import UnitedStates

class Alabama(UnitedStates):
    include_confederation_day: bool
    martin_luther_king_label: ClassVar[str]
    presidents_day_label: ClassVar[str]
    columbus_day_label: ClassVar[str]
    include_jefferson_davis_birthday: bool

class AlabamaBaldwinCounty(Alabama):
    include_fat_tuesday: bool

class AlabamaMobileCounty(Alabama):
    include_fat_tuesday: bool

class AlabamaPerryCounty(Alabama):
    def get_obama_day(self, year): ...
    def get_variable_days(self, year): ...
