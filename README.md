# AWS Facial Recognition System
A facial recognition system built with AWS services for employee registration and visitor authentication. This system leverages AWS Rekognition for facial detection and feature extraction, providing secure and scalable identity verification.

## How It Works

![Architecture](https://github.com/user-attachments/assets/85568a89-0644-4c4d-b03c-096bc6259617)

https://github.com/user-attachments/assets/d631e85e-e81f-42f2-ae39-606820eb9f05

## Key Idea

The system uses a serverless architecture with the following AWS services:

- **Amazon S3**: Image storage and Lambda function triggers
- **AWS Rekognition**: Facial detection and feature extraction  
- **AWS Lambda**: Serverless image processing (registration - saving employee data to DynamoDB & authentication - verifying visitors against stored data)  
- **Amazon DynamoDB**: Metadata and face print storage 
- **API Gateway**: Deploying REST API endpoints for frontend access
- **Frontend**: Simple react app to call the API endpoint
