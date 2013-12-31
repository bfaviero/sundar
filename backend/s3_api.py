import subprocess, os, sys
from datetime import datetime
from glob import glob

import boto
import boto.s3
from boto.s3.key import Key
from boto.exception import S3ResponseError
from boto.s3.connection import S3Connection

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

IMAGES_BUCKET_NAME = 'sundar.io.pictures'
AUDIO_BUCKET_NAME = 'sundar.io.audio'
VIDEO_BUCKET_NAME = 'sundar.io.video'

def get_bucket(name):
    try:
        bucket = conn.get_bucket(name)
    except S3ResponseError, e:
        if e.status == 403:
            sys.exit('Error: Check your Amazon credentials.')
        elif e.status == 404:
            #bucket does not exist, create it
            bucket = conn.create_bucket(name, location=boto.s3.connection.Location.DEFAULT)
    return bucket

def percent_complete(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def info(name):
    buckets = conn.get_all_buckets()
    print "There are %s total buckets:" % len(buckets)
    for bucket in buckets:
        print "Files in %s" % bucket.name 
        bucket = get_bucket()
        print "In the bucket %s:" % name    
        for key in bucket:
            print key.name.encode('utf-8')


