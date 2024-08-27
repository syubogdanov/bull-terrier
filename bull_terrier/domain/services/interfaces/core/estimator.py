import sys

from typing import TYPE_CHECKING, Protocol


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from bull_terrier.domain.entities.math.probability import Probability


class Estimator(Protocol):
    """The estimator protocol."""

    def __call__(self: Self, lhs: str, rhs: str) -> "Probability":
        """
        Estimate the probability that `lhs` is a plagiarism of `rhs`.

        Parameters
        ----------
        lhs : str
            Text.
        rhs : str
            Text.

        Returns
        -------
        Probability
            Probability estimation.
        """
