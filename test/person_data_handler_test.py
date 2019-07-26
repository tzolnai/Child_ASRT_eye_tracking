#    Copyright (C) <2019>  <Tamás Zolnai>    <zolnaitamas2000@gmail.com>

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

import sys
# Add the local path to the main script so we can import it.
sys.path = [".."] + sys.path

import os
import shelve, dbm, codecs
import asrt
import time

class personDataHandlerTest(unittest.TestCase):

    def tearDown(self):
        tempdir = os.path.abspath(__file__)
        (tempdir, trail) = os.path.split(tempdir)
        tempdir = os.path.join(tempdir, "data", "person_data_handler")

        # remove all temp files
        for file in os.listdir(tempdir):
            file_path = os.path.join(tempdir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    def setUp(self):
        tempdir = os.path.abspath(__file__)
        (tempdir, trail) = os.path.split(tempdir)
        tempdir = os.path.join(tempdir, "data", "person_data_handler")
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

    def constructFilePath(self, file_name):
        this_file_path = os.path.abspath(__file__)
        file_path = os.path.split(this_file_path)[0]
        file_path = os.path.join(file_path, "data")
        file_path = os.path.join(file_path, "person_data_handler")
        file_path = os.path.join(file_path, file_name)
        return file_path

    def testRoundTripPersonSettings(self):
        all_settings_file_path = self.constructFilePath("testRoundTripSettings")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", all_settings_file_path, "", "", "")

        PCodes = {1: '3rd - 1324'}
        stim_output_line = 1
        stim_sessionN = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimepoch = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimblock = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimtrial = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15}
        stimlist = {1: 3, 2: 1, 3: 2, 4: 3, 5: 2, 6: 2, 7: 2, 8: 4, 9: 1, 10: 1, 11: 4, 12: 3, 13: 3, 14: 2, 15: 2}
        stimpr = {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'P', 7: 'R', 8: 'P', 9: 'R', 10: 'P', 11: 'R', 12: 'P', 13: 'R', 14: 'P', 15: 'R'}
        last_N = 1
        end_at = {1: 16, 2: 16, 3: 16, 4: 16, 5: 16, 6: 16, 7: 16, 8: 16, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16, 14: 16, 15: 16}
        stim_colorN = {1: 'Orange', 2: 'Orange', 3: 'Orange', 4: 'Orange', 5: 'Orange', 6: 'Orange', 7: 'Orange', 8: 'Orange', 9: 'Orange', 10: 'Orange', 11: 'Orange', 12: 'Orange', 13: 'Orange', 14: 'Orange', 15: 'Orange'}

        person_data_handler.save_person_settings(PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN)

        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", all_settings_file_path, "", "", "")

        PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN = person_data_handler.load_person_settings()

        self.assertEqual(PCodes, {1: '3rd - 1324'})
        self.assertEqual(stim_output_line, 1)
        self.assertEqual(stim_sessionN, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1})
        self.assertEqual(stimepoch, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1})
        self.assertEqual(stimblock, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1})
        self.assertEqual(stimtrial, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15})
        self.assertEqual(stimlist, {1: 3, 2: 1, 3: 2, 4: 3, 5: 2, 6: 2, 7: 2, 8: 4, 9: 1, 10: 1, 11: 4, 12: 3, 13: 3, 14: 2, 15: 2})
        self.assertEqual(stimpr, {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'P', 7: 'R', 8: 'P', 9: 'R', 10: 'P', 11: 'R', 12: 'P', 13: 'R', 14: 'P', 15: 'R'})
        self.assertEqual(last_N, 1)
        self.assertEqual(end_at, {1: 16, 2: 16, 3: 16, 4: 16, 5: 16, 6: 16, 7: 16, 8: 16, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16, 14: 16, 15: 16})
        self.assertEqual(stim_colorN, {1: 'Orange', 2: 'Orange', 3: 'Orange', 4: 'Orange', 5: 'Orange', 6: 'Orange', 7: 'Orange', 8: 'Orange', 9: 'Orange', 10: 'Orange', 11: 'Orange', 12: 'Orange', 13: 'Orange', 14: 'Orange', 15: 'Orange'})

    def testReadMissingPersonSettings(self):
        all_settings_file_path = self.constructFilePath("testReadMissingPersonSettings")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", all_settings_file_path, "", "", "")

        PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN = person_data_handler.load_person_settings()

        self.assertEqual(PCodes, {})
        self.assertEqual(stim_output_line, 0)
        self.assertEqual(stim_sessionN, {})
        self.assertEqual(stimepoch, {})
        self.assertEqual(stimblock, {})
        self.assertEqual(stimtrial, {})
        self.assertEqual(stimlist, {})
        self.assertEqual(stimpr, {})
        self.assertEqual(last_N, 0)
        self.assertEqual(end_at, {})
        self.assertEqual(stim_colorN, {})

    def testReadIncompletePersonSettings(self):
        all_settings_file_path = self.constructFilePath("testReadIncompletePersonSettings")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", all_settings_file_path, "", "", "")

        # save something, but not all settings
        with shelve.open(all_settings_file_path, 'n') as all_settings_file:
            this_person_settings = {}
            this_person_settings[ 'PCodes' ] = {1: '3rd - 1324'}
            this_person_settings[ 'stim_output_line' ] = 12

            all_settings = {}
            all_settings["alattomos-aladar_333_group1"] = this_person_settings

            all_settings_file['all_settings'] = all_settings

        PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN = person_data_handler.load_person_settings()

        self.assertEqual(PCodes, {})
        self.assertEqual(stim_output_line, 0)
        self.assertEqual(stim_sessionN, {})
        self.assertEqual(stimepoch, {})
        self.assertEqual(stimblock, {})
        self.assertEqual(stimtrial, {})
        self.assertEqual(stimlist, {})
        self.assertEqual(stimpr, {})
        self.assertEqual(last_N, 0)
        self.assertEqual(end_at, {})
        self.assertEqual(stim_colorN, {})

    def testUpdateExistingPersonSettings(self):
        all_settings_file_path = self.constructFilePath("testUpdateExistingPersonSettings")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", all_settings_file_path, "", "", "")

        PCodes = {1: '3rd - 1324'}
        stim_output_line = 1
        stim_sessionN = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimepoch = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimblock = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        stimtrial = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15}
        stimlist = {1: 3, 2: 1, 3: 2, 4: 3, 5: 2, 6: 2, 7: 2, 8: 4, 9: 1, 10: 1, 11: 4, 12: 3, 13: 3, 14: 2, 15: 2}
        stimpr = {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'P', 7: 'R', 8: 'P', 9: 'R', 10: 'P', 11: 'R', 12: 'P', 13: 'R', 14: 'P', 15: 'R'}
        last_N = 1
        end_at = {1: 16, 2: 16, 3: 16, 4: 16, 5: 16, 6: 16, 7: 16, 8: 16, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16, 14: 16, 15: 16}
        stim_colorN = {1: 'Orange', 2: 'Orange', 3: 'Orange', 4: 'Orange', 5: 'Orange', 6: 'Orange', 7: 'Orange', 8: 'Orange', 9: 'Orange', 10: 'Orange', 11: 'Orange', 12: 'Orange', 13: 'Orange', 14: 'Orange', 15: 'Orange'}

        person_data_handler.save_person_settings(PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN)

        stim_output_line = 41
        last_N = 32
        person_data_handler.save_person_settings(PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN)

        PCodes, stim_output_line, stim_sessionN, stimepoch, stimblock, stimtrial, stimlist, stimpr, last_N, end_at, stim_colorN = person_data_handler.load_person_settings()

        self.assertEqual(stim_output_line, 41)
        self.assertEqual(last_N, 32)

    def testCreateIDsFiles(self):
        all_IDs_file_path = self.constructFilePath("testCreateIDsFiles")
        subject_list_file_path = self.constructFilePath("testCreateIDsFiles.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", all_IDs_file_path, subject_list_file_path, "")

        person_data_handler.update_subject_IDs_files()

        # output files exist
        self.assertTrue(os.path.exists(all_IDs_file_path + ".dat"))
        self.assertTrue(os.path.exists(subject_list_file_path))

        with shelve.open(all_IDs_file_path) as all_IDs_file:
            all_IDs = all_IDs_file['ids']
            self.assertEqual(all_IDs, ["alattomos-aladar_333_group1"])

        with codecs.open(subject_list_file_path,'r', encoding = 'utf-8') as subject_list_txt:
            self.assertEqual(subject_list_txt.read(), "alattomos-aladar\t333\tgroup1\n")

    def testAddSameIDToIDsFiles(self):
        all_IDs_file_path = self.constructFilePath("testAddSameIDToIDsFiles")
        subject_list_file_path = self.constructFilePath("testAddSameIDToIDsFiles.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", all_IDs_file_path, subject_list_file_path, "")

        # call this twice simulating of running the experiment with the same subject more times
        person_data_handler.update_subject_IDs_files()
        person_data_handler.update_subject_IDs_files()

        # output files exist
        self.assertTrue(os.path.exists(all_IDs_file_path + ".dat"))
        self.assertTrue(os.path.exists(subject_list_file_path))

        with shelve.open(all_IDs_file_path) as all_IDs_file:
            all_IDs = all_IDs_file['ids']
            self.assertEqual(all_IDs, ["alattomos-aladar_333_group1"])

        with codecs.open(subject_list_file_path,'r', encoding = 'utf-8') as subject_list_txt:
            self.assertEqual(subject_list_txt.read(), "alattomos-aladar\t333\tgroup1\n")

    def testAddMoreIDsToIDsFiles(self):
        all_IDs_file_path = self.constructFilePath("testAddMoreIDsToIDsFiles")
        subject_list_file_path = self.constructFilePath("testAddMoreIDsToIDsFiles.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", all_IDs_file_path, subject_list_file_path, "")
        person_data_handler.update_subject_IDs_files()

        person_data_handler = asrt.PersonDataHandler("toth-csaba_111_group2", "", all_IDs_file_path, subject_list_file_path, "")
        person_data_handler.update_subject_IDs_files()

        person_data_handler = asrt.PersonDataHandler("kertesz-bela_222_group3", "", all_IDs_file_path, subject_list_file_path, "")
        person_data_handler.update_subject_IDs_files()

        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", all_IDs_file_path, subject_list_file_path, "")
        person_data_handler.update_subject_IDs_files()

        # output files exist
        self.assertTrue(os.path.exists(all_IDs_file_path + ".dat"))
        self.assertTrue(os.path.exists(subject_list_file_path))

        with shelve.open(all_IDs_file_path) as all_IDs_file:
            all_IDs = all_IDs_file['ids']
            self.assertEqual(all_IDs, ["alattomos-aladar_333_group1", 'toth-csaba_111_group2', 'kertesz-bela_222_group3'])

        with codecs.open(subject_list_file_path,'r', encoding = 'utf-8') as subject_list_txt:
            self.assertEqual(subject_list_txt.read(), "alattomos-aladar\t333\tgroup1\n"
                                                      "toth-csaba\t111\tgroup2\n"
                                                      "kertesz-bela\t222\tgroup3\n")

    def testSaveSpecialGroupNameToIDsFiles(self):
        all_IDs_file_path = self.constructFilePath("testSaveSpecialGroupNameToIDsFiles")
        subject_list_file_path = self.constructFilePath("testSaveSpecialGroupNameToIDsFiles.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group_1", "", all_IDs_file_path, subject_list_file_path, "")
        person_data_handler.update_subject_IDs_files()

        # output files exist
        self.assertTrue(os.path.exists(all_IDs_file_path + ".dat"))
        self.assertTrue(os.path.exists(subject_list_file_path))

        with shelve.open(all_IDs_file_path) as all_IDs_file:
            all_IDs = all_IDs_file['ids']
            self.assertEqual(all_IDs, ["alattomos-aladar_333_group_1"])

        with codecs.open(subject_list_file_path,'r', encoding = 'utf-8') as subject_list_txt:
            self.assertEqual(subject_list_txt.read(), "alattomos-aladar\t333\tgroup_1\n")

    def testAppendToEmptyOutput(self):
        output_file_path = self.constructFilePath("testAppendToEmptyOutput.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group_1", "", "", "", output_file_path)

        person_data_handler.append_to_output_file("something")

        with codecs.open(output_file_path,'r', encoding = 'utf-8') as output_file:
            self.assertEqual(output_file.read(), "computer_name\tGroup\tSubject_ID\tSubject_nr\tasrt_type\tPCode\toutput_line\t"
                                                 "session\tepoch\tblock\ttrial\tRSI_time\tframe_rate\tframe_time\tframe_sd\t"
                                                 "date\ttime\tstimulus_color\tPR\tRT\terror\tstimulus\tstimbutton\tquit_log\tsomething")

    def testAppendMoreTimesToOutput(self):
        output_file_path = self.constructFilePath("testAppendMoreTimesToOutput.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group_1", "", "", "", output_file_path)

        person_data_handler.append_to_output_file("\nsomething")
        person_data_handler.append_to_output_file("\nsomething2")
        person_data_handler.append_to_output_file("\nsomething3")

        with codecs.open(output_file_path,'r', encoding = 'utf-8') as output_file:
            self.assertEqual(output_file.read(), "computer_name\tGroup\tSubject_ID\tSubject_nr\tasrt_type\tPCode\toutput_line\t"
                                                 "session\tepoch\tblock\ttrial\tRSI_time\tframe_rate\tframe_time\tframe_sd\t"
                                                 "date\ttime\tstimulus_color\tPR\tRT\terror\tstimulus\tstimbutton\tquit_log\t\n"
                                                 "something\nsomething2\nsomething3")

    def testWriteEmptyOutput(self):
        output_file_path = self.constructFilePath("testWriteEmptyOutput.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", "", "", output_file_path)

        computer_name = "Laposka"
        group = "group1"
        identif = "alattomos-aladar"
        subject_nr = 333
        asrt_type = "implicit"
        PCode = "1234"
        stim_output_line = 12
        session = 1
        epoch = 2
        block = 12
        trial = 21
        stim_RSI = 0.123
        frame_rate = 59.1
        frame_time = 16.56
        frame_sd = 1.3
        stim_RT_time = time.strftime('%H:%M:%S')
        stim_RT_date = time.strftime('%d/%m/%Y')
        stim_color = "Orange"
        stimpr = "P"
        stimRT = 321.2345
        stimACC = 0
        stimulus = 1
        stimbutton = 'z'

        person_data_handler.write_data_to_output(computer_name, group, identif, subject_nr, asrt_type, PCode, stim_output_line,
                             session, epoch, block, trial, stim_RSI, frame_rate, frame_time, frame_sd, stim_RT_time,
                             stim_RT_date, stim_color, stimpr, stimRT, stimACC, stimulus, stimbutton)

        with codecs.open(output_file_path,'r', encoding = 'utf-8') as output_file:
            self.assertEqual(output_file.read(), "computer_name\tGroup\tSubject_ID\tSubject_nr\tasrt_type\tPCode\toutput_line\t"
                                                 "session\tepoch\tblock\ttrial\tRSI_time\tframe_rate\tframe_time\tframe_sd\t"
                                                 "date\ttime\tstimulus_color\tPR\tRT\terror\tstimulus\tstimbutton\tquit_log\t\n"
                                                 "Laposka\tgroup1\talattomos-aladar\t333\timplicit\t1234\t12\t1\t2\t"
                                                 "12\t21\t0,123\t59,1\t16,56\t1,3\t" + str(stim_RT_time) + "\t" + str(stim_RT_date) + "\t"
                                                 "Orange\tP\t321,2345\t0\t1\tz\t")

    def testWriteExistingOutput(self):
        output_file_path = self.constructFilePath("testWriteExistingOutput.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", "", "", output_file_path)

        computer_name = "Laposka"
        group = "group1"
        identif = "alattomos-aladar"
        subject_nr = 333
        asrt_type = "implicit"
        PCode = "1234"
        stim_output_line = 12
        session = 1
        epoch = 2
        block = 12
        trial = 21
        stim_RSI = 0.123
        frame_rate = 59.1
        frame_time = 16.56
        frame_sd = 1.3
        stim_RT_time = time.strftime('%H:%M:%S')
        stim_RT_date = time.strftime('%d/%m/%Y')
        stim_color = "Orange"
        stimpr = "P"
        stimRT = 321.2345
        stimACC = 0
        stimulus = 1
        stimbutton = 'z'

        person_data_handler.write_data_to_output(computer_name, group, identif, subject_nr, asrt_type, PCode, stim_output_line,
                             session, epoch, block, trial, stim_RSI, frame_rate, frame_time, frame_sd, stim_RT_time,
                             stim_RT_date, stim_color, stimpr, stimRT, stimACC, stimulus, stimbutton)

        stim_output_line = 13
        trial = 22
        stim_RSI = 0.111
        stim_RT_time = time.strftime('%H:%M:%S')
        stim_RT_date = time.strftime('%d/%m/%Y')
        stim_color = "Green"
        stimpr = "R"
        stimRT = 523.2345
        stimACC = 1
        stimulus = 2
        stimbutton = 'b'

        person_data_handler.write_data_to_output(computer_name, group, identif, subject_nr, asrt_type, PCode, stim_output_line,
                             session, epoch, block, trial, stim_RSI, frame_rate, frame_time, frame_sd, stim_RT_time,
                             stim_RT_date, stim_color, stimpr, stimRT, stimACC, stimulus, stimbutton)

        with codecs.open(output_file_path,'r', encoding = 'utf-8') as output_file:
            self.assertEqual(output_file.read(), "computer_name\tGroup\tSubject_ID\tSubject_nr\tasrt_type\tPCode\toutput_line\t"
                                                 "session\tepoch\tblock\ttrial\tRSI_time\tframe_rate\tframe_time\tframe_sd\t"
                                                 "date\ttime\tstimulus_color\tPR\tRT\terror\tstimulus\tstimbutton\tquit_log\t\n"
                                                 "Laposka\tgroup1\talattomos-aladar\t333\timplicit\t1234\t12\t1\t2\t"
                                                 "12\t21\t0,123\t59,1\t16,56\t1,3\t" + str(stim_RT_time) + "\t" + str(stim_RT_date) + "\t"
                                                 "Orange\tP\t321,2345\t0\t1\tz\t\n"
                                                 "Laposka\tgroup1\talattomos-aladar\t333\timplicit\t1234\t13\t1\t2\t"
                                                 "12\t22\t0,111\t59,1\t16,56\t1,3\t" + str(stim_RT_time) + "\t" + str(stim_RT_date) + "\t"
                                                 "Green\tR\t523,2345\t1\t2\tb\t")

    def testPointInComputerNameOrDate(self):
        output_file_path = self.constructFilePath("testPointInComputerName.txt")
        person_data_handler = asrt.PersonDataHandler("alattomos-aladar_333_group1", "", "", "", output_file_path)

        computer_name = "I. Richárd"
        group = "group1"
        identif = "alattomos-aladar"
        subject_nr = 333
        asrt_type = "implicit"
        PCode = "1234"
        stim_output_line = 12
        session = 1
        epoch = 2
        block = 12
        trial = 21
        stim_RSI = 0.123
        frame_rate = 59.1
        frame_time = 16.56
        frame_sd = 1.3
        stim_RT_time = time.strftime('%H:%M:%S')
        stim_RT_date = time.strftime('%Y.%m.%d')
        stim_color = "Orange"
        stimpr = "P"
        stimRT = 321.2345
        stimACC = 0
        stimulus = 1
        stimbutton = 'z'

        person_data_handler.write_data_to_output(computer_name, group, identif, subject_nr, asrt_type, PCode, stim_output_line,
                             session, epoch, block, trial, stim_RSI, frame_rate, frame_time, frame_sd, stim_RT_time,
                             stim_RT_date, stim_color, stimpr, stimRT, stimACC, stimulus, stimbutton)

        with codecs.open(output_file_path,'r', encoding = 'utf-8') as output_file:
            self.assertEqual(output_file.read(), "computer_name\tGroup\tSubject_ID\tSubject_nr\tasrt_type\tPCode\toutput_line\t"
                                                 "session\tepoch\tblock\ttrial\tRSI_time\tframe_rate\tframe_time\tframe_sd\t"
                                                 "date\ttime\tstimulus_color\tPR\tRT\terror\tstimulus\tstimbutton\tquit_log\t\n"
                                                 "I. Richárd\tgroup1\talattomos-aladar\t333\timplicit\t1234\t12\t1\t2\t"
                                                 "12\t21\t0,123\t59,1\t16,56\t1,3\t" + str(stim_RT_time) + "\t" + str(stim_RT_date) + "\t"
                                                 "Orange\tP\t321,2345\t0\t1\tz\t")

if __name__ == "__main__":
    unittest.main() # run all tests