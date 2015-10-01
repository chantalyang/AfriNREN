from django.core.management.base import BaseCommand, CommandError
import csv
from AfriNREN_Vis.models import Flow
from datetime import datetime, timedelta
import sys
import random
import json


class Command(BaseCommand):
    help = 'Creates and saves random data'

    def handle(self, *args, **options):
        # read in AS details
        ASes = []
        nodes = []
        links = []
        filename = 'AS-details.csv'
        csvfilepath = '/Users/rob/dev/AfriNREN-NetFLOW-Scripts/%s' % filename
        jsonfilepath = '/Users/rob/dev/AfriNREN/AfriNREN_Vis/static/data/randomdata.txt'
        self.stdout.write('**loading AS data**')
        with open(csvfilepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                ASes.append(row)
        # choose random set of ASes
        for x in range(0, 30):
            nodes.append(random.choice(ASes))
        # Assign group numbers to all of the nodes with 3 - 6 nodes per group
        for x in range(1, 21):
            for y in range(3, 7):
                random.choice(nodes)['group'] = x
        # Give 'bytes' to random nodes
        for x in range(1, 10):
            random.choice(nodes)['bytes'] = random.randint(1000000000, 19000000000)
        # create links between each node pair in the group
        for x in range(1, 21):
            grouplist = []
            for y in range(len(nodes)):
                try:
                    if nodes[y]['group'] == x:
                        grouplist.append([nodes[y], y])
                except KeyError:
                    continue
            for z in range(0, len(grouplist)-1):
                links.append({'source': grouplist[z][1],
                              'target': grouplist[z+1][1]})

        # write nodes and links to file
        data = {'nodes': nodes,
                'links': links}

        with open(jsonfilepath, 'w') as outfile:
            json.dump(data, outfile)
