from datetime import datetime, timezone, timedelta
from typing import Hashable, Any


class TimeTracker:
    @staticmethod
    def get_current_datetime() -> datetime:
        """current time in the USA (Eastern Time Zone)"""
        return datetime.now(timezone(timedelta(hours=-5)))

    @staticmethod
    def is_within_same_day(old_timestamp: datetime) -> bool:
        current_time_usa = TimeTracker.get_current_datetime()

        return old_timestamp.date() == current_time_usa.date()


class ResponseGenerator:
    @staticmethod
    def prototype(**kwargs) -> dict[Hashable, Any]:
        """Dynamically generates a dict and returns it. Accepts only keywords arguments."""

        _result = {}
        given_kwargs = locals()['kwargs']

        for kwarg_key, kwarg_val in given_kwargs.items():
            _result[kwarg_key] = kwarg_val

        return _result
