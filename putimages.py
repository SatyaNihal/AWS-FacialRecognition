
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image_01.jpg','Nihal Kodukula'),
      ('image_02.jpg','Nihal Kodukula'),
      ('image_03.jpg','Nihal Kodukula'),
      ('image_04.jpg','Cristiano Ronaldo'),
      ('image_05.jpg','Cristiano Ronaldo'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('resident-imgs-5','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})