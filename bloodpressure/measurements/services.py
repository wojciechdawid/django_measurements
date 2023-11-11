from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from faker import Faker

faker = Faker("pl_PL")


@dataclass
class Measurement:
    id: int
    date: datetime
    systolic: int
    diastolic: int

class IMeasurementService(ABC):

    def list() -> list[Measurement]:
        pass

class FakeMeasurementService(IMeasurementService):

    @classmethod
    def _create_measurement(cls) -> Measurement:
        n = 25
        measurements_list = []
        for i in range(n):
            systolic = faker.random.randint(60, 250)
            diastolic = faker.random.randint(30, 180)
            measurements_list.append(Measurement(
                id=i+1,
                date=faker.date(),
                systolic=systolic,
                diastolic=diastolic
            ))
        return measurements_list

    def list() -> list[Measurement]:
        return FakeMeasurementService._create_measurement()
