import subprocess, os, sys
from datetime import datetime
from glob import glob

import boto
import boto.s3
from boto.s3.key import Key
from boto.exception import S3ResponseError
from boto.s3.connection import S3Connection

#AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
#AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

#conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
conn = boto.connect_s3()
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

def info():
    buckets = conn.get_all_buckets()
    print "There are %s total buckets:" % len(buckets)
    for bucket in buckets:
        print "Files in %s" % bucket.name 
        bucket = get_bucket()
        #print "In the bucket %s:" % name
        for key in bucket:
            print key.name.encode('utf-8')

def upload_image(image, supplier_id, item_id):
    bucket = get_bucket(IMAGES_BUCKET_NAME)
    bucket_key = Key(bucket)
    time_stamp = datetime.now().strftime("%y%m%d_%H%M%S")
    bucket_key.key = supplier_id + "." + item_id + "." + time_stamp
    #print 'Uploading with bucket key %s to Amazon S3 bucket %s' % (bucket_key.name.encode('utf-8'), IMAGES_BUCKET_NAME)
    #image_stream = StringIO.StringIO(image.read())
    #bucket_key.set_contents_from_file(image_stream)
    bucket_key.set_contents_from_string(image.read(), cb=percent_complete, num_cb=10)
    bucket_key.set_metadata('Content-Type', 'image/jpeg')
    bucket_key.set_acl('public-read')
    #bucket_key.make_public()
    url = bucket_key.generate_url(expires_in=None, query_auth=False)
    #k.get_contents_to_filename('download.tar.gz')
    #print 'Upload complete.'
    return url