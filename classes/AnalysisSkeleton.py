import boto
import boto.s3.connection
import pandas as pd

class analysisSkeleton:

    def __init__(self, data):
        self.data=data

    def getAttribute(self):
        return self.data

    def cleanData(self):
        s=self.data['lineStatuses']
        self.data['statusSeverity']=s.iloc[:].apply(lambda x: x[0]['statusSeverity'])
        self.data['statusSeverityDescription']=s.iloc[:].apply(lambda x: x[0]['statusSeverityDescription'])
        self.data['validityPeriods']=s.iloc[:].apply(lambda x: x[0]['validityPeriods'])
        self.data['created2']=s.iloc[:].apply(lambda x: x[0]['created'])
        self.data['line']=s.iloc[:].apply(lambda x: x[0]['id'])
        del self.data['name']
        del self.data['id']
        #del data['lineStatuses']
        #del data['routeSections']

        # todo
        # refactor so function can be run repeatedly
        # created2==??\
        # plot delays *
        # why is it always good service

        return self.data
