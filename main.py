import json
import os
import time
import random
import urllib.request

from featureflags.client import CfClient
from featureflags.config import with_base_url, with_events_url
from featureflags.evaluations.auth_target import Target
from featureflags.util import log

# Constants: API Configuration
# Replace the API KEY, dude! That is just an example! Here you may override all these constants via the environment
# variables, which are the 1st argument on the `os.environ.get` method.
API_KEY = os.environ.get('FF_API_KEY', "33302433-5da8-4186-a6a3-6c4d5917a313")
BASE_URL = os.environ.get('FF_BASE_URL', "https://config.ff.harness.io/api/1.0")
EVENTS_URL = os.environ.get('FF_EVENTS_URL', "https://events.ff.harness.io/api/1.0")
IP_INFO_URL = os.environ.get('FF_IP_INFO_URL', 'http://ipinfo.io/json')


# Constants: Client Configuration
# Here I will do the same for the Harness Feature Flags Client ID and Name, because I don't know your use case.
def generate_random_string(length=10):
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.@_-"
    return ''.join(random.choice(allowed_chars) for _ in range(length))


CLIENT_ID = os.environ.get('FF_CLIENT_ID', f"gabs{generate_random_string()}")
CLIENT_NAME = os.environ.get('FF_CLIENT_NAME', "Gabs the Harnessian")


def get_client_data_based_on_src_ip():
    """
    Fetch client data based on source IP.
    :return: A dictionary containing metadata about the client.
    """
    response = urllib.request.urlopen(IP_INFO_URL)
    data = json.load(response)

    return {
        'src_ip': data['ip'],
        'org': data['org'],
        'city': data['city'],
        'country': data['country'],
        'region': data['region']
    }


def setup_client(api_key, base_url, events_url):
    """
    Setup and return a CfClient instance.
    :param api_key: API key for authentication.
    :param base_url: Base URL for the client.
    :param events_url: Events URL for the client.
    :return: An instance of CfClient.
    """
    return CfClient(api_key, with_base_url(base_url), with_events_url(events_url))


def main():
    log.debug("Starting example")

    client = setup_client(API_KEY, BASE_URL, EVENTS_URL)

    attributes = {
        "location": "LATAM",
        "tier": "humble/poor dude",
        "country": "Brazil",
        "pet": "Bart"
    }
    attributes.update(get_client_data_based_on_src_ip())

    target = Target(identifier=CLIENT_ID, name=CLIENT_NAME, attributes=attributes)

    while True:
        result = client.json_variation('gabriel', target, {})
        log.debug(f"Result {result}")
        time.sleep(5)


if __name__ == "__main__":
    main()
