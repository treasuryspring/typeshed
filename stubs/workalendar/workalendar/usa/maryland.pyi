from .core import UnitedStates

class Maryland(UnitedStates):
    thanksgiving_friday_label: ClassVar[str]
    include_thanksgiving_friday: bool
    def get_variable_days(self, year): ...
