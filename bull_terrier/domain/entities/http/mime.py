from enum import Enum


class MIME:
    """Internet data according to the `MIME` standard."""

    class Application(str, Enum):
        """The internal format of the application program."""

        ZIP = "application/zip"
        GZIP = "application/gzip"

    class Text(str, Enum):
        """Text."""

        PLAIN = "text/plain"

    class VND(str, Enum):
        """Vendor files."""

        RAR = "application/vnd.rar"

    class X(str, Enum):
        """Non-standard files."""

        RAR = "application/x-rar-compressed"
        TAR = "application/x-tar"
        ZIP = "application/x-zip-compressed"
