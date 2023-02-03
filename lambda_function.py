# import relevant modules
import boto3
import csv


def lambda_handler(event, context):
    # read s3 bucket name and file name from test event
    bucket_name = event['bucket']
    file_name = event['file']

    # create csv file in lambda tmp folder
    with open('/tmp/' + file_name, 'w+') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write the header
        writer.writerow(['id', 'name', 'date', 'age'])

        # write the data
        writer.writerow([1, 'anuradha', '02/02/2023', '28'])
        writer.writerow([2, 'prabhath', '04/02/2023', '30'])

    s3_path = 'uploads/' + file_name

    s3 = boto3.resource("s3")
    # upload csv file from lambda tmp folder to s3 bucket
    s3.Bucket(bucket_name).upload_file('/tmp/' + file_name, s3_path)
