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

#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-

import unittest

import os

import sys
# Add the local path to the main script so we can import it.
sys.path = [".."] + [os.path.join("..", "externals", "psychopy_mock")]  + sys.path

import asrt
import shutil

import psychopy_gui_mock as pgm

dict_accents = {u'á':u'a',u'é':u'e',u'í':u'i',u'ó':u'o',u'ő':u'o',u'ö':u'o',u'ú':u'u',u'ű':u'u',u'ü':u'u'}

class participantIDTest(unittest.TestCase):

    def tearDown(self):
        tempdir = os.path.abspath(__file__)
        (tempdir, trail) = os.path.split(tempdir)
        tempdir = os.path.join(tempdir, "data", "participant_id")

        # remove all temp files
        for file in os.listdir(tempdir):
            file_path = os.path.join(tempdir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def constructFilePath(self, file_name):
        filepath = os.path.abspath(__file__)
        (filepath, trail) = os.path.split(filepath)
        filepath = os.path.join(filepath, "data", "participant_id", file_name)
        return filepath

    def testNoSettingsFile(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(['Tóth Béla', 10, 'kontrol', '3rd - 1324', '2nd - 1243'])

        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.groups = ["kontrol", "exp1"]
        exp_settings.numsessions = 2
        exp_settings.epochN = 2
        exp_settings.epochs = [1, 1]
        exp_settings.block_in_epochN = 2
        exp_settings.blockprepN = 5
        exp_settings.blocklengthN = 20
        exp_settings.asrt_rcolor = "Orange"
        exp_settings.asrt_pcolor = "Green"
        exp_settings.asrt_types = {}
        exp_settings.asrt_types[1] = "implicit"
        exp_settings.asrt_types[2] = "implicit"

        thispath = self.constructFilePath("NoSettingsFile")
        asrt.ensure_dir(os.path.join(thispath, "settings"))

        group, subject_nr, identif, person_data_handler, PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, last_N, end_at, stim_colorN, stimpr = asrt.participant_id(thispath, exp_settings, dict_accents)

        self.assertEqual(group, 'kontrol')
        self.assertEqual(subject_nr, 10)
        self.assertEqual(identif, "toth-bela")
        self.assertEqual(PCodes, {1: '3rd - 1324', 2: '2nd - 1243'})
        self.assertEqual(stim_output_line, 0)
        self.assertEqual(stim_sessionN, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(stimepoch, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(stimblock, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 33: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 2, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3, 61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 4, 87: 4, 88: 4, 89: 4, 90: 4, 91: 4, 92: 4, 93: 4, 94: 4, 95: 4, 96: 4, 97: 4, 98: 4, 99: 4, 100: 4})
        self.assertEqual(stimtrial, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 1, 27: 2, 28: 3, 29: 4, 30: 5, 31: 6, 32: 7, 33: 8, 34: 9, 35: 10, 36: 11, 37: 12, 38: 13, 39: 14, 40: 15, 41: 16, 42: 17, 43: 18, 44: 19, 45: 20, 46: 21, 47: 22, 48: 23, 49: 24, 50: 25, 51: 1, 52: 2, 53: 3, 54: 4, 55: 5, 56: 6, 57: 7, 58: 8, 59: 9, 60: 10, 61: 11, 62: 12, 63: 13, 64: 14, 65: 15, 66: 16, 67: 17, 68: 18, 69: 19, 70: 20, 71: 21, 72: 22, 73: 23, 74: 24, 75: 25, 76: 1, 77: 2, 78: 3, 79: 4, 80: 5, 81: 6, 82: 7, 83: 8, 84: 9, 85: 10, 86: 11, 87: 12, 88: 13, 89: 14, 90: 15, 91: 16, 92: 17, 93: 18, 94: 19, 95: 20, 96: 21, 97: 22, 98: 23, 99: 24, 100: 25})
        self.assertEqual(len(stimlist), 100)
        self.assertEqual(last_N, 0)
        self.assertEqual(end_at, {1: 51, 2: 51, 3: 51, 4: 51, 5: 51, 6: 51, 7: 51, 8: 51, 9: 51, 10: 51, 11: 51, 12: 51, 13: 51, 14: 51, 15: 51, 16: 51, 17: 51, 18: 51, 19: 51, 20: 51, 21: 51, 22: 51, 23: 51, 24: 51, 25: 51, 26: 51, 27: 51, 28: 51, 29: 51, 30: 51, 31: 51, 32: 51, 33: 51, 34: 51, 35: 51, 36: 51, 37: 51, 38: 51, 39: 51, 40: 51, 41: 51, 42: 51, 43: 51, 44: 51, 45: 51, 46: 51, 47: 51, 48: 51, 49: 51, 50: 51, 51: 101, 52: 101, 53: 101, 54: 101, 55: 101, 56: 101, 57: 101, 58: 101, 59: 101, 60: 101, 61: 101, 62: 101, 63: 101, 64: 101, 65: 101, 66: 101, 67: 101, 68: 101, 69: 101, 70: 101, 71: 101, 72: 101, 73: 101, 74: 101, 75: 101, 76: 101, 77: 101, 78: 101, 79: 101, 80: 101, 81: 101, 82: 101, 83: 101, 84: 101, 85: 101, 86: 101, 87: 101, 88: 101, 89: 101, 90: 101, 91: 101, 92: 101, 93: 101, 94: 101, 95: 101, 96: 101, 97: 101, 98: 101, 99: 101, 100: 101})
        self.assertEqual(stim_colorN, {1: 'Orange', 2: 'Orange', 3: 'Orange', 4: 'Orange', 5: 'Orange', 6: 'Orange', 7: 'Orange', 8: 'Orange', 9: 'Orange', 10: 'Orange', 11: 'Orange', 12: 'Orange', 13: 'Orange', 14: 'Orange', 15: 'Orange', 16: 'Orange', 17: 'Orange', 18: 'Orange', 19: 'Orange', 20: 'Orange', 21: 'Orange', 22: 'Orange', 23: 'Orange', 24: 'Orange', 25: 'Orange', 26: 'Orange', 27: 'Orange', 28: 'Orange', 29: 'Orange', 30: 'Orange', 31: 'Orange', 32: 'Orange', 33: 'Orange', 34: 'Orange', 35: 'Orange', 36: 'Orange', 37: 'Orange', 38: 'Orange', 39: 'Orange', 40: 'Orange', 41: 'Orange', 42: 'Orange', 43: 'Orange', 44: 'Orange', 45: 'Orange', 46: 'Orange', 47: 'Orange', 48: 'Orange', 49: 'Orange', 50: 'Orange', 51: 'Orange', 52: 'Orange', 53: 'Orange', 54: 'Orange', 55: 'Orange', 56: 'Orange', 57: 'Orange', 58: 'Orange', 59: 'Orange', 60: 'Orange', 61: 'Orange', 62: 'Orange', 63: 'Orange', 64: 'Orange', 65: 'Orange', 66: 'Orange', 67: 'Orange', 68: 'Orange', 69: 'Orange', 70: 'Orange', 71: 'Orange', 72: 'Orange', 73: 'Orange', 74: 'Orange', 75: 'Orange', 76: 'Orange', 77: 'Orange', 78: 'Orange', 79: 'Orange', 80: 'Orange', 81: 'Orange', 82: 'Orange', 83: 'Orange', 84: 'Orange', 85: 'Orange', 86: 'Orange', 87: 'Orange', 88: 'Orange', 89: 'Orange', 90: 'Orange', 91: 'Orange', 92: 'Orange', 93: 'Orange', 94: 'Orange', 95: 'Orange', 96: 'Orange', 97: 'Orange', 98: 'Orange', 99: 'Orange', 100: 'Orange'})
        self.assertEqual(stimpr, {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'P', 7: 'R', 8: 'P', 9: 'R', 10: 'P', 11: 'R', 12: 'P', 13: 'R', 14: 'P', 15: 'R', 16: 'P', 17: 'R', 18: 'P', 19: 'R', 20: 'P', 21: 'R', 22: 'P', 23: 'R', 24: 'P', 25: 'R', 26: 'R', 27: 'R', 28: 'R', 29: 'R', 30: 'R', 31: 'P', 32: 'R', 33: 'P', 34: 'R', 35: 'P', 36: 'R', 37: 'P', 38: 'R', 39: 'P', 40: 'R', 41: 'P', 42: 'R', 43: 'P', 44: 'R', 45: 'P', 46: 'R', 47: 'P', 48: 'R', 49: 'P', 50: 'R', 51: 'R', 52: 'R', 53: 'R', 54: 'R', 55: 'R', 56: 'P', 57: 'R', 58: 'P', 59: 'R', 60: 'P', 61: 'R', 62: 'P', 63: 'R', 64: 'P', 65: 'R', 66: 'P', 67: 'R', 68: 'P', 69: 'R', 70: 'P', 71: 'R', 72: 'P', 73: 'R', 74: 'P', 75: 'R', 76: 'R', 77: 'R', 78: 'R', 79: 'R', 80: 'R', 81: 'P', 82: 'R', 83: 'P', 84: 'R', 85: 'P', 86: 'R', 87: 'P', 88: 'R', 89: 'P', 90: 'R', 91: 'P', 92: 'R', 93: 'P', 94: 'R', 95: 'P', 96: 'R', 97: 'P', 98: 'R', 99: 'P', 100: 'R'})

        # Check person data handler's properties too
        self.assertEqual(person_data_handler.subject_id, "toth-bela_10_kontrol")
        self.assertEqual(person_data_handler.all_settings_file_path, os.path.join(thispath, "settings", person_data_handler.subject_id))
        self.assertEqual(person_data_handler.all_IDs_file_path, os.path.join(thispath, "settings", "participant_settings"))
        self.assertEqual(person_data_handler.subject_list_file_path, os.path.join(thispath, "settings", "participants_in_experiment.txt"))
        self.assertEqual(person_data_handler.output_file_path, os.path.join(thispath, "logs", person_data_handler.subject_id + "_log.txt"))

        # Some files were created
        self.assertTrue(os.path.isfile(person_data_handler.all_settings_file_path + ".dat"))
        self.assertTrue(os.path.isfile(person_data_handler.all_IDs_file_path + ".dat"))
        self.assertTrue(os.path.isfile(person_data_handler.subject_list_file_path))

    def testExistingSettingsFile(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(['Tóth Béla', 10, 'kontrol', '3rd - 1324', '2nd - 1243', 'Tóth Béla', 10, 'kontrol'])

        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.groups = ["kontrol", "exp1"]
        exp_settings.numsessions = 2
        exp_settings.epochN = 2
        exp_settings.epochs = [1, 1]
        exp_settings.block_in_epochN = 2
        exp_settings.blockprepN = 5
        exp_settings.blocklengthN = 20
        exp_settings.asrt_rcolor = "Orange"
        exp_settings.asrt_pcolor = "Green"
        exp_settings.asrt_types = {}
        exp_settings.asrt_types[1] = "implicit"
        exp_settings.asrt_types[2] = "implicit"

        thispath = self.constructFilePath("NoSettingsFile")
        asrt.ensure_dir(os.path.join(thispath, "settings"))

        # call once to get the participant settings
        group, subject_nr, identif, person_data_handler, PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, last_N, end_at, stim_colorN, stimpr = asrt.participant_id(thispath, exp_settings, dict_accents)

        # let save participant settings after the first block
        last_N = 25
        person_data_handler.save_person_settings(PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN)

        exp_settings = asrt.ExperimentSettings("", "")
        exp_settings.groups = ["kontrol", "exp1"]
        exp_settings.epochN = 2
        exp_settings.block_in_epochN = 2
        exp_settings.blockprepN = 5
        exp_settings.blocklengthN = 20

        # now load back the participant's settings with participant id function
        group, subject_nr, identif, person_data_handler, PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, last_N, end_at, stim_colorN, stimpr = asrt.participant_id(thispath, exp_settings, dict_accents)

        self.assertEqual(group, 'kontrol')
        self.assertEqual(subject_nr, 10)
        self.assertEqual(identif, "toth-bela")
        self.assertEqual(PCodes, {1: '3rd - 1324', 2: '2nd - 1243'})
        self.assertEqual(stim_output_line, 0)
        self.assertEqual(stim_sessionN, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(stimepoch, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(stimblock, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 33: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 2, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3, 61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 4, 87: 4, 88: 4, 89: 4, 90: 4, 91: 4, 92: 4, 93: 4, 94: 4, 95: 4, 96: 4, 97: 4, 98: 4, 99: 4, 100: 4})
        self.assertEqual(stimtrial, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 1, 27: 2, 28: 3, 29: 4, 30: 5, 31: 6, 32: 7, 33: 8, 34: 9, 35: 10, 36: 11, 37: 12, 38: 13, 39: 14, 40: 15, 41: 16, 42: 17, 43: 18, 44: 19, 45: 20, 46: 21, 47: 22, 48: 23, 49: 24, 50: 25, 51: 1, 52: 2, 53: 3, 54: 4, 55: 5, 56: 6, 57: 7, 58: 8, 59: 9, 60: 10, 61: 11, 62: 12, 63: 13, 64: 14, 65: 15, 66: 16, 67: 17, 68: 18, 69: 19, 70: 20, 71: 21, 72: 22, 73: 23, 74: 24, 75: 25, 76: 1, 77: 2, 78: 3, 79: 4, 80: 5, 81: 6, 82: 7, 83: 8, 84: 9, 85: 10, 86: 11, 87: 12, 88: 13, 89: 14, 90: 15, 91: 16, 92: 17, 93: 18, 94: 19, 95: 20, 96: 21, 97: 22, 98: 23, 99: 24, 100: 25})
        self.assertEqual(len(stimlist), 100)
        self.assertEqual(last_N, 25)
        self.assertEqual(end_at, {1: 51, 2: 51, 3: 51, 4: 51, 5: 51, 6: 51, 7: 51, 8: 51, 9: 51, 10: 51, 11: 51, 12: 51, 13: 51, 14: 51, 15: 51, 16: 51, 17: 51, 18: 51, 19: 51, 20: 51, 21: 51, 22: 51, 23: 51, 24: 51, 25: 51, 26: 51, 27: 51, 28: 51, 29: 51, 30: 51, 31: 51, 32: 51, 33: 51, 34: 51, 35: 51, 36: 51, 37: 51, 38: 51, 39: 51, 40: 51, 41: 51, 42: 51, 43: 51, 44: 51, 45: 51, 46: 51, 47: 51, 48: 51, 49: 51, 50: 51, 51: 101, 52: 101, 53: 101, 54: 101, 55: 101, 56: 101, 57: 101, 58: 101, 59: 101, 60: 101, 61: 101, 62: 101, 63: 101, 64: 101, 65: 101, 66: 101, 67: 101, 68: 101, 69: 101, 70: 101, 71: 101, 72: 101, 73: 101, 74: 101, 75: 101, 76: 101, 77: 101, 78: 101, 79: 101, 80: 101, 81: 101, 82: 101, 83: 101, 84: 101, 85: 101, 86: 101, 87: 101, 88: 101, 89: 101, 90: 101, 91: 101, 92: 101, 93: 101, 94: 101, 95: 101, 96: 101, 97: 101, 98: 101, 99: 101, 100: 101})
        self.assertEqual(stim_colorN, {1: 'Orange', 2: 'Orange', 3: 'Orange', 4: 'Orange', 5: 'Orange', 6: 'Orange', 7: 'Orange', 8: 'Orange', 9: 'Orange', 10: 'Orange', 11: 'Orange', 12: 'Orange', 13: 'Orange', 14: 'Orange', 15: 'Orange', 16: 'Orange', 17: 'Orange', 18: 'Orange', 19: 'Orange', 20: 'Orange', 21: 'Orange', 22: 'Orange', 23: 'Orange', 24: 'Orange', 25: 'Orange', 26: 'Orange', 27: 'Orange', 28: 'Orange', 29: 'Orange', 30: 'Orange', 31: 'Orange', 32: 'Orange', 33: 'Orange', 34: 'Orange', 35: 'Orange', 36: 'Orange', 37: 'Orange', 38: 'Orange', 39: 'Orange', 40: 'Orange', 41: 'Orange', 42: 'Orange', 43: 'Orange', 44: 'Orange', 45: 'Orange', 46: 'Orange', 47: 'Orange', 48: 'Orange', 49: 'Orange', 50: 'Orange', 51: 'Orange', 52: 'Orange', 53: 'Orange', 54: 'Orange', 55: 'Orange', 56: 'Orange', 57: 'Orange', 58: 'Orange', 59: 'Orange', 60: 'Orange', 61: 'Orange', 62: 'Orange', 63: 'Orange', 64: 'Orange', 65: 'Orange', 66: 'Orange', 67: 'Orange', 68: 'Orange', 69: 'Orange', 70: 'Orange', 71: 'Orange', 72: 'Orange', 73: 'Orange', 74: 'Orange', 75: 'Orange', 76: 'Orange', 77: 'Orange', 78: 'Orange', 79: 'Orange', 80: 'Orange', 81: 'Orange', 82: 'Orange', 83: 'Orange', 84: 'Orange', 85: 'Orange', 86: 'Orange', 87: 'Orange', 88: 'Orange', 89: 'Orange', 90: 'Orange', 91: 'Orange', 92: 'Orange', 93: 'Orange', 94: 'Orange', 95: 'Orange', 96: 'Orange', 97: 'Orange', 98: 'Orange', 99: 'Orange', 100: 'Orange'})
        self.assertEqual(stimpr, {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'P', 7: 'R', 8: 'P', 9: 'R', 10: 'P', 11: 'R', 12: 'P', 13: 'R', 14: 'P', 15: 'R', 16: 'P', 17: 'R', 18: 'P', 19: 'R', 20: 'P', 21: 'R', 22: 'P', 23: 'R', 24: 'P', 25: 'R', 26: 'R', 27: 'R', 28: 'R', 29: 'R', 30: 'R', 31: 'P', 32: 'R', 33: 'P', 34: 'R', 35: 'P', 36: 'R', 37: 'P', 38: 'R', 39: 'P', 40: 'R', 41: 'P', 42: 'R', 43: 'P', 44: 'R', 45: 'P', 46: 'R', 47: 'P', 48: 'R', 49: 'P', 50: 'R', 51: 'R', 52: 'R', 53: 'R', 54: 'R', 55: 'R', 56: 'P', 57: 'R', 58: 'P', 59: 'R', 60: 'P', 61: 'R', 62: 'P', 63: 'R', 64: 'P', 65: 'R', 66: 'P', 67: 'R', 68: 'P', 69: 'R', 70: 'P', 71: 'R', 72: 'P', 73: 'R', 74: 'P', 75: 'R', 76: 'R', 77: 'R', 78: 'R', 79: 'R', 80: 'R', 81: 'P', 82: 'R', 83: 'P', 84: 'R', 85: 'P', 86: 'R', 87: 'P', 88: 'R', 89: 'P', 90: 'R', 91: 'P', 92: 'R', 93: 'P', 94: 'R', 95: 'P', 96: 'R', 97: 'P', 98: 'R', 99: 'P', 100: 'R'})

if __name__ == "__main__":
    unittest.main() # run all tests