import sys
from datatailr.scheduler import Job, EntryPoint, JobType
from service import main as service_main
from app import main as app_main

arg = sys.argv[1] if len(sys.argv) > 1 else 'service'

if arg == 'service':
    job = Job(
        "test_service",
        type=JobType.SERVICE,
        entrypoint=EntryPoint(
            type=JobType.SERVICE,
            func=service_main,
        ),
        run_as="an",
    )
    job.save()
elif arg == 'app':
    job = Job(
        "test_app",
        type=JobType.APP,
        entrypoint=EntryPoint(
            type=JobType.APP,
            func=app_main,
        ),
        run_as="an",
    )
    job.save()
else:
    print("Unknown argument. Use 'app' or 'service'.")