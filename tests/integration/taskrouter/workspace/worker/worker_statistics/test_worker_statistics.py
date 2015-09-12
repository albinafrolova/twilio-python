# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.taskrouter.client import TaskrouterClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class StatisticsIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "activity_durations": [
                    {
                        "avg": 0.0,
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Busy",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Idle",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Offline",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Reserved",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    }
                ],
                "end_time": "2015-08-18T16:36:19Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:21:19Z",
                "tasks_assigned": 0
            },
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.get("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "Minutes": 1,
                "StartDate": "2008-01-02"
            },
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = TaskrouterClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "cumulative": {
                "activity_durations": [
                    {
                        "avg": 0.0,
                        "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Busy",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Idle",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Offline",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    },
                    {
                        "avg": 0.0,
                        "friendly_name": "Reserved",
                        "max": 0,
                        "min": 0,
                        "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "total": 0
                    }
                ],
                "end_time": "2015-08-18T16:36:19Z",
                "reservations_accepted": 0,
                "reservations_canceled": 0,
                "reservations_created": 0,
                "reservations_rejected": 0,
                "reservations_rescinded": 0,
                "reservations_timed_out": 0,
                "start_time": "2015-08-18T16:21:19Z",
                "tasks_assigned": 0
            },
            "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .workspaces.get("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .workers.get("WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .statistics.get(
                minutes=1,
                start_date=datetime(2008, 1, 2, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0)
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.worker_sid)
        self.assertEqual(u"WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.worker_sid)
        self.assertIsNotNone(instance.workspace_sid)
        self.assertEqual(u"WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.workspace_sid)