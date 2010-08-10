#!/usr/bin/python2.5

# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gtfsobjectbase import GtfsObjectBase
from persistable import Persistable

class Frequency(GtfsObjectBase, Persistable):
    """This class represents a period of a trip during which the vehicle travels
    at regular intervals (rather than specifying exact times for each stop)."""

    _REQUIRED_FIELD_NAMES = ['trip_id', 'start_time', 'end_time',
                             'headway_secs']
    _FIELD_NAMES = _REQUIRED_FIELD_NAMES
    _TABLE_NAME = "frequencies"

    _SQL_TABLENAME = _TABLE_NAME 
    _SQL_FIELD_TYPES = ["CHAR(50)", "CHAR(10)", "CHAR(10)", "INTEGER"]
    _SQL_FIELDS = zip( _FIELD_NAMES, _SQL_FIELD_TYPES )

    def __init__(self, field_dict=None):
      Persistable.__init__(self, None)

      self._schedule = None
      if not field_dict:
        return
      self.trip_id = field_dict['trip_id']
      self.start_time = field_dict['start_time']
      self.end_time = field_dict['end_time']
      self.headway_secs = field_dict['headway_secs']

    def StartTime(self):
      return self.start_time

    def EndTime(self):
      return self.end_time

    def TripId(self):
      return self.trip_id

    def HeadwaySecs(self):
      return self.headway_secs

    def ValidateBeforeAdd(self, problems):
      return True

    def ValidateAfterAdd(self, problems):
      return

    def Validate(self, problems=None):
      return

    def AddToSchedule(self, schedule=None, problems=None):
      if schedule is None:
        return
      self._schedule = schedule
      try:
        trip = schedule.GetTrip(self.trip_id)
      except KeyError:
        problems.InvalidValue('trip_id', self.trip_id)
        return
      trip.AddFrequencyObject(self, problems)
