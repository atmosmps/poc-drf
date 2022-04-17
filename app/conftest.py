import os

import pytest
import vcr
from testfixtures import LogCapture

VCR_CASSETTES_DIR = os.path.join(os.path.dirname(__file__), "vcr")


@pytest.fixture(scope="session")
def vcr_client():
    return vcr.VCR(
        serializer="json",
        cassette_library_dir=VCR_CASSETTES_DIR,
        record_mode="once",
        match_on=["uri", "method", "query", "headers", "body"],
    )


@pytest.fixture()
def log_capture():
    with LogCapture() as capture:
        yield capture
