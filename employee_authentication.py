import boto3
import json

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition', region_name='ca-central-1')
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')

employeeTable = dynamodb.Table('employee')
bucketName = 'nihal-visitor-image-storage'

def lambda_handler(event, context):
    try:
        print('Event:', json.dumps(event))
        objectKey = event['queryStringParameters']['objectKey']

        s3_response = s3.get_object(Bucket=bucketName, Key=objectKey)
        image_bytes = s3_response['Body'].read()

        rekog_response = rekognition.search_faces_by_image(
            CollectionId='employees',
            Image={'Bytes': image_bytes}
        )

        print("Rekognition response:", json.dumps(rekog_response, indent=2))

        for match in rekog_response.get('FaceMatches', []):
            face_id = match['Face']['FaceId']
            confidence = match['Face']['Confidence']

            if confidence >= 90:
                print(f"Match found: FaceId={face_id}, Confidence={confidence}")
                face_record = employeeTable.get_item(Key={'rekognitionId': face_id})
                
                if 'Item' in face_record:
                    item = face_record['Item']
                    return buildResponse(200, {
                        'Message': 'Success',
                        'firstName': item.get('firstName', ''),
                        'lastName': item.get('lastName', '')
                    })

        return buildResponse(403, {'Message': 'Person not found'})

    except Exception as e:
        print('Error:', str(e))
        return buildResponse(500, {'Message': 'Internal server error'})

def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response
