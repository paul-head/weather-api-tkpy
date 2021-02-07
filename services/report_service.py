import datetime
import uuid
from typing import List

from models.location import Location
from models.reports import Report

__reports: List[Report] = []


async def get_report() -> List[Report]:

    # would be async call here
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(id=str(uuid.uuid4()),
                    location=location,
                    description=description,
                    created_date=now)

    # would be async call here
    __reports.append(report)
    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report
