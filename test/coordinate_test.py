# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
# Add the local path to the main script and external scripts so we can import them.
sys.path = [".."] + sys.path

import unittest
from psychopy import visual, monitors, core
import asrt
import platform


class coordinateTest(unittest.TestCase):

    def initWindow(self):
        self.my_monitor = monitors.Monitor('myMon')
        self.my_monitor.setSizePix([1366, 768])
        self.my_monitor.setWidth(29)
        self.my_monitor.saveMon()

        if platform.system() == "Linux":
            win_type = 'pygame'
        else:
            win_type = 'pyglet'

        return visual.Window(size=[1366, 768],
                             pos=[0, 0],
                             units='cm',
                             fullscr=False,
                             allowGUI=True,
                             monitor=self.my_monitor,
                             winType=win_type,
                             color='White',
                             gammaRamp=256,
                             gammaErrorPolicy='ignore')

    def testTopRightPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((0.0, 0.0))
            self.assertAlmostEqual(result[0], -23.8, delta=0.001)
            self.assertAlmostEqual(result[1], 13.38, delta=0.001)

    def testCenterPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((0.5, 0.5))
            self.assertAlmostEqual(result[0], 0.0, delta=0.001)
            self.assertAlmostEqual(result[1], 0.0, delta=0.001)

    def testTopLeftPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((1.0, 0.0))
            self.assertAlmostEqual(result[0], 23.8, delta=0.001)
            self.assertAlmostEqual(result[1], 13.38, delta=0.001)

    def testBottomLeftPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((0.0, 1.0))
            self.assertAlmostEqual(result[0], -23.8, delta=0.001)
            self.assertAlmostEqual(result[1], -13.38, delta=0.001)

    def testBottomRightPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((1.0, 1.0))
            self.assertAlmostEqual(result[0], 23.8, delta=0.001)
            self.assertAlmostEqual(result[1], -13.38, delta=0.001)

    def testCustomPos(self):
        experiment = asrt.Experiment("")
        with self.initWindow() as experiment.mywindow:
            experiment.mymonitor = self.my_monitor
            experiment.settings = asrt.ExperimentSettings("", "")
            experiment.settings.monitor_width = 47.6

            result = experiment.ADCS_to_PCMCS((0.33, 0.67))
            self.assertAlmostEqual(result[0], -8.091, delta=0.001)
            self.assertAlmostEqual(result[1], -4.549, delta=0.001)


if __name__ == "__main__":
    unittest.main()  # run all tests
