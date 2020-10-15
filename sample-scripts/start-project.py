# USAGE
# python3 start-project.py [PROJECT-ARN] [MIN-INFERENCE-UNITS (OPTIONAL - DEFAULT:1)]

import boto3
import sys

client = boto3.client('rekognition')

def start_project_version(projectVersionArn, minInferenceUnits):
  try:
    res = client.start_project_version(ProjectVersionArn=projectVersionArn, MinInferenceUnits=minInferenceUnits)
    return res['Status']
  except Exception as err:
    print(err)
    return 'ERROR'
#end start_project_version

if(len(sys.argv) > 1):# python3 start-project.py arn:aws:rekognition:[region]:[account-number]:project/[project-name]/version/[project-version]
  projectVersionArn = sys.argv[1]
else:
  print('ERROR: ProjectARN is required.')
  quit()
#end if

if(len(sys.argv) > 2):
  minInferenceUnits = sys.argv[2]
else:
  minInferenceUnits = 1
#end if

stat = start_project_version(projectVersionArn, minInferenceUnits)
print("Status:{0}".format(stat))