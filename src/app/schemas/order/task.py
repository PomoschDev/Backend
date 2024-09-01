from enum import Enum


class Task(str, Enum):
    Money = "Money"
    Service = "Service"
    Product = "Product"
    Job = "Job"
