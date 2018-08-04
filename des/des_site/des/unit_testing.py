# -*- coding: utf-8 -*-
import unittest
import simulation
import datetime

class TestTimeToMinutes(unittest.TestCase):
  def runTest(self):
    assert simulation.time_to_minutes(datetime.time(1,30)) ==  