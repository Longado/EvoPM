"""EvoPM public package."""

from .model import Recommendation, TaskProfile
from .triage import recommend

__all__ = ["Recommendation", "TaskProfile", "recommend"]
__version__ = "0.1.0"
