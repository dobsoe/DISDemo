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
        del data['name']
        del data['id']
        #del data['lineStatuses']
        #del data['routeSections']
        return data
