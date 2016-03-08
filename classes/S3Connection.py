import boto
import boto.s3.connection
import pandas as pd

class s3Connection:

    def __init__(self):
        self.access_key = 'AKIAJYA6PMAUGLR37S4Q'
        self.secret_key = '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'
        self.bucket='pivotal-london-dis'
        self.testkey='tfl_api_line_mode_status_tube_2015-02-24_11:51:45.json'

    def getjson_test(self):
        conn = boto.s3.connect_to_region('eu-west-1',
                                          aws_access_key_id = self.access_key,
                                          aws_secret_access_key = self.secret_key,
                                          calling_format = boto.s3.connection.OrdinaryCallingFormat(),)
        bucket_dis=conn.get_bucket(self.bucket)
        key=bucket_dis.get_key(self.testkey)
        data = key.get_contents_as_string()
        return data

    def getjson(self, maxfiles=-1):
        conn = boto.s3.connect_to_region('eu-west-1',
                                          aws_access_key_id = self.access_key,
                                          aws_secret_access_key = self.secret_key,
                                          calling_format = boto.s3.connection.OrdinaryCallingFormat(),)
        bucket_dis=conn.get_bucket(self.bucket)

        i=0
        for key in bucket_dis.list():
            i=i+1
            if(i%100==0):
                print (str(i)+'files read')
            if((maxfiles>0) and (i>maxfiles)):
                break
            key=bucket_dis.get_key(key.name.encode('utf-8'))
            df=pd.read_json(key.get_contents_as_string())
            if i==1:
                data=df
            else:
                data=pd.concat([data,df])
        print 'done'
        return data
