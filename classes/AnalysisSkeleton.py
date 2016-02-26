import boto
import boto.s3.connection
import pandas as pd

class analysisSkeleton:

    def __init__(self, jsondata):
        print jsondata
        self.data=jsondata

    def getAttribute(self):
        return str(self.data)
