from datatailr.scheduler import Job, EntryPoint, JobType
from app import main

service = Job(
    "test_service",
    type=JobType.SERVICE,
    entrypoint=EntryPoint(
        type=JobType.SERVICE,
        func=main,
    ),
    run_as="an",
)
service.save()