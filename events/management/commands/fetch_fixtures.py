from __future__ import absolute_import

import requests
from datetime import timedelta
from dateutil.parser import parse
from django.core.management.base import BaseCommand, CommandError

from events.models import Event


LFC_FIXTURES = "http://api.football-data.org/alpha/teams/64/fixtures"

headers = {
    "Accept": "application/json",
    "X-Auth-Token": "817d7c8d5aad4f7c9708fc7488b1530a"
}

LOCATION = "Meehan\'s Downtown\n200 Peachtree St NE\nAtlanta, GA 30303"
EXTERNAL_URL = "http://www.meehansdowntown.com/"

TEMPLATE = """
<h2>Matchday {day}: {title}</h2>
<br />
<p>Please join LFC Atlanta to watch {home} (home) take on {away} (away)</p>
<p>Current LFC Atlanta members get priority access and seating at Meehan's. YNWA!</p>
"""

class Command(BaseCommand):
    help = "fetch LFC fixtures and save as Events"

    def handle(self, *args, **options):
        try:
            response = requests.get(LFC_FIXTURES, headers=headers)
            data = response.json()
            if 'fixtures' in data.keys():
                fixtures = data['fixtures']
                for match in fixtures:
                    start_date = parse(match['date'])
                    stop_date = start_date + timedelta(hours=2)
                    home_team = match['homeTeamName']
                    away_team = match['awayTeamName']
                    matchday = match['matchday']
                    title = "%s vs %s" % (home_team, away_team)
                    content = TEMPLATE.format(day=matchday, title=title, home=home_team, away=away_team)
                    try:
                        event = Event.objects.get(title=title, start=start_date, end=stop_date)
                        event.content = content
                        event.save()
                    except Event.DoesNotExist:
                        event = Event.objects.create(
                            title=title,
                            start=start_date,
                            end=stop_date,
                            content=content,
                            location=LOCATION,
                            external_url=EXTERNAL_URL
                        )
                    print "Saved '%s'" % event
        except Exception as e:
            print e
