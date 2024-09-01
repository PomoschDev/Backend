from enum import Enum


class Collect(str, Enum):
    Monthly = "Monthly"
    One_time = "One-time"
    Emergency = "Emergency"
    General = "General"
