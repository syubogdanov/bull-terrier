import sys

from pydantic import Field


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


Probability = Annotated[float, Field(ge=0.0, le=1.0)]
