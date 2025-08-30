# AWS Facial Recognition System


## How It Works

A facial recognition system built with AWS services for employee registration and visitor authentication. This system leverages AWS Rekognition for facial detection and feature extraction, providing secure and scalable identity verification.

## Key Idea

The system uses a serverless architecture with the following AWS services:

- **Amazon S3**: Image storage and Lambda function triggers
- **AWS Rekognition**: Facial detection and feature extraction  
- **AWS Lambda**: Serverless image processing (registration - saving employee data to DynamoDB & authentication - verifying visitors against stored data)  
- **Amazon DynamoDB**: Metadata and face print storage 
- **API Gateway**: Deploying REST API endpoints for frontend access