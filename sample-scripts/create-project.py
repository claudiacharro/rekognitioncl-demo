# USAGE
# Provide a PROJECT NAME to create a NEW PROJECT and a NEW PROJECT VERSION
# python3 create-project.py [BUCKET-NAME] [DATASET-NAME] [OBJECT-VERSION] [PROJECT-NAME (OPTIONAL, Default: "PRJ+TIMESTAMP")] [VERSION-NAME (OPTIONAL, Default:"V1")]
# 
# Provide a PROJECT ARN to create a NEW PROJECT VERSION without creating a new project.
# python3 create-project.py [BUCKET-NAME] [DATASET-NAME] [OBJECT-VERSION] [PROJECT-ARN] [VERSION-NAME (OPTIONAL, Default:"V1")]

import boto3
import sys
import datetime

client = boto3.client('rekognition')

def create_project(projectName):
    res = client.create_project(ProjectName=projectName)
    return res['ProjectArn']
#end create_project

def create_project_version(projectArn, versionName, bucket, objectVersion, dsName):
    versionName += datetime.datetime.now(datetime.timezone.utc).strftime("-%d%m%Y-%H%M%S%f")
    outputConfig = {
        "S3Bucket": bucket,
        "S3KeyPrefix": "/datasets/{0}".format(dsName)
    }
    trainingData = {
        "Assets": [{
            "GroundTruthManifest": {
                "S3Object": {
                    "Bucket": bucket,
                    "Name": "datasets/{0}/manifests/output/output.manifest".format(dsName),
                    "Version": objectVersion
                }
            }
        }]
    }
    testingData = {"AutoCreate": True}
    res = client.create_project_version(ProjectArn=projectArn,
                                        VersionName=versionName,
                                        OutputConfig=outputConfig,
                                        TrainingData=trainingData,
                                        TestingData=testingData)
    return res["ProjectVersionArn"]

#end create_project_version

if(len(sys.argv) > 1):
  bucket = sys.argv[1]
else:
  print('ERROR: Bucket name is required.')
  quit()
#end if

if(len(sys.argv) > 2):
  dsName = sys.argv[2]
else:
  print('ERROR: Dataset name is required.')
  quit()
#end if

if(len(sys.argv) > 3): 
  objectVersion = sys.argv[3]
else:
  objectVersion = ""
#end if

if(len(sys.argv) > 4): 
  projectName = sys.argv[4]
else:
  projectName = "PRJ" + datetime.datetime.now(datetime.timezone.utc).strftime("-%d%m%Y-%H%M%S%f")
#end if

if(len(sys.argv) > 4): 
  versionName = sys.argv[5]
else:
  versionName = "V1"
#end if

if(projectName.startswith("arn:aws")):
  projectArn = projectName
else:
  projectArn = create_project(projectName)
  print("New Project ARN: {0}".format(projectArn))
#end if

projectVersionArn = create_project_version(projectArn, versionName, bucket, objectVersion, dsName)
print("New Project Version ARN: {0}".format(projectVersionArn))

