# USAGE
# python3 stop-project.py [PROJECT-ARN]

import boto3
import sys

client = boto3.client('rekognition')

def stop_project_version(projectVersionArn):

    try:
        res = client.stop_project_version(ProjectVersionArn=projectVersionArn)
        return res['Status']
    except Exception as err:
        print(err)
        return 'ERROR'
        return res['Status']

#end start_project_version

if (len(sys.argv) > 1):# python3 stop-project.py [PROJECT-ARN]
    projectVersionArn = sys.argv[1]
else:
    print('ERROR: ProjectARN is required.')
    quit()
#end if

stat = stop_project_version(projectVersionArn)
print("Status:{0}".format(stat))