from datetime import datetime, timezone, timedelta


class TimeTracker:
    @staticmethod
    def get_current_datetime() -> datetime:
        """current time in the USA (Eastern Time Zone)"""
        return datetime.now(timezone(timedelta(hours=-5)))

    @staticmethod
    def is_within_same_day(previous_time: datetime) -> bool:
        current_time_usa = TimeTracker.get_current_datetime()

        return previous_time.date() == current_time_usa.date()
