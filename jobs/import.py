#!/usr/bin/env python

"""
    Script to import data from .csv file to Model Database DJango
    To execute this script run: 
    1) manage.py shell
    2) exec(open('import.py').read())
"""

import csv
from jobs.models import Job

CSV_PATH = './jobs/jobs.csv'      # Csv file path  


with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in spamreader:
        Job.objects.create(batch_number=row[0], submitted_at=row[1] if row[1] else None, nodes_used=row[2] or None)
        # Example -> Book.objects.create(ISBNCode=row[0], title=row[1], author=row[2])
        # csv_data.date = row[0] if row[0] else datetime.datetime.today()