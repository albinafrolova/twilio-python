# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.base import TwilioClient
from twilio.rest.resources import UNSET_TIMEOUT
from twilio.rest.pricing.voice import Voices
from twilio.rest.pricing.phone_number import PhoneNumbers


class PricingClient(TwilioClient):
    """
    A client for accessing the Twilio Pricing API.
    
    :param str account: :param str account: Your Account SID from `your
    dashboard
        <https://twilio.com/user/account>`_
    :param str timeout: :param float timeout: The socket connect and read
    timeout
        for requests to Twilio
    :param str token: :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    """

    def __init__(self, account=None, token=None, base="https://pricing.twilio.com",
                 version="v1", timeout=UNSET_TIMEOUT, client=None):
        super(PricingClient, self).__init__(account, token, base, version, timeout, client)
        
        self.version_uri = "{}/{}".format(base, version)
        self.voice = Voices(self.client, self.version_uri, self.auth, self.timeout)
        self.phone_numbers = PhoneNumbers(self.client, self.version_uri, self.auth, self.timeout)