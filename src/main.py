import os
from enum import Enum

DRY_RUN = os.environ.get("DRY_RUN")


class DryRun(Enum):
    TRUE = 'TRUE'
    FALSE = 'FALSE'


def lambda_handler(event, context):
    if DRY_RUN == DryRun.TRUE.value:
        print("[INFO] Hello world, dry run!")
    else:
        print("[INFO] Hello world!")
