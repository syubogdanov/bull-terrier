from datetime import datetime, timezone


def utcnow() -> datetime:
    """Return the current UTC date and time."""
    return datetime.now(timezone.utc)
