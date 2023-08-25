from _typeshed import Incomplete

from ..core import WesternCalendar

class Monaco(WesternCalendar):
    include_easter_monday: ClassVar[bool]
    include_ascension: ClassVar[bool]
    include_whit_monday: ClassVar[bool]
    include_all_saints: ClassVar[bool]
    include_assumption: ClassVar[bool]
    include_corpus_christi: ClassVar[bool]
    include_immaculate_conception: ClassVar[bool]
    include_labour_day: ClassVar[bool]
    FIXED_HOLIDAYS: Incomplete
