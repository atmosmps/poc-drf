import pytest
from unittest.mock import Mock


@pytest.fixture
def ip_stack_http_client_failure_response():
    request = Mock()
    request.status_code = 200
    request.json = {
        "success": False,
        "error": {
            "code": 104,
            "type": "usage_limit_reached",
            "info": "Your monthly usage limit has been reached. Please upgrade your Subscription Plan.",
        },
    }
    return request


@pytest.fixture
def ip_stack_http_client_successfully_response():
    request = Mock()
    request.status_code = 200
    request.json = {
        "ip": "134.201.250.155",
        "hostname": "134.201.250.155",
        "type": "ipv4",
        "continent_code": "NA",
        "continent_name": "North America",
        "country_code": "US",
        "country_name": "United States",
        "region_code": "CA",
        "region_name": "California",
        "city": "Los Angeles",
        "zip": "90013",
        "latitude": 34.0453,
        "longitude": -118.2413,
        "location": {
            "geoname_id": 5368361,
            "capital": "Washington D.C.",
            "languages": [{"code": "en", "name": "English", "native": "English"}],
            "country_flag": "https://assets.ipstack.com/images/assets/flags_svg/us.svg",
            "country_flag_emoji": "🇺🇸",
            "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
            "calling_code": "1",
            "is_eu": "false",
        },
        "time_zone": {
            "id": "America/Los_Angeles",
            "current_time": "2018-03-29T07:35:08-07:00",
            "gmt_offset": -25200,
            "code": "PDT",
            "is_daylight_saving": "true",
        },
        "currency": {
            "code": "USD",
            "name": "US Dollar",
            "plural": "US dollars",
            "symbol": "$",
            "symbol_native": "$",
        },
        "connection": {"asn": 25876, "isp": "Los Angeles Department of Water & Power"},
        "security": {
            "is_proxy": "false",
            "proxy_type": "null",
            "is_crawler": "false",
            "crawler_name": "null",
            "crawler_type": "null",
            "is_tor": "false",
            "threat_level": "low",
            "threat_types": "null",
        },
    }
    return request