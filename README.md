# E-commerce-website-using-AWS

This project is an e-commerce website where users can browse products, add them to the cart, and place an order. When an order is placed, the order details are stored automatically in an AWS DynamoDB table using AWS Lambda, API Gateway, and IAM roles.

Steps to Set Up the Website

Step 1: Create an S3 Bucket for Hosting

Go to AWS S3 → Click Create Bucket.

Set a unique Bucket Name and Region.

Enable Static Website Hosting and upload index.html, product.html, and checkout.html.

Make sure the bucket policy allows public access for reading.

Step 2: Create a DynamoDB Table for Orders

Go to AWS DynamoDB → Click Create Table.

Set Table Name: Orders.

Set Primary Key: order_id (String).

Click Create Table.

Step 3: Create an AWS Lambda Function

Go to AWS Lambda → Click Create Function.

Choose Author from Scratch.

Set Function Name: StoreOrder.

Choose Runtime: Python 3.x.

Add the required permissions:

AmazonDynamoDBFullAccess

AWSLambdaBasicExecutionRole

Write a Lambda function to receive data from the API Gateway and store it in DynamoDB.

Step 4: Set Up API Gateway

Go to AWS API Gateway → Click Create API.

Choose REST API → Click Build.

Create a new resource and new method (POST).

Integrate it with the Lambda Function (StoreOrder).

Deploy the API to a stage (e.g., prod).

Copy the Invoke URL for use in the frontend.

Step 5: Connect the Checkout Page to API Gateway

Update checkout.html to send order details to API Gateway.

Use JavaScript's fetch() method to call the API.

When a user clicks "Place Order," the order details are sent to the API Gateway.

The API Gateway triggers Lambda, which stores the order in DynamoDB.

Step 6: Test the Setup

Open the website hosted on S3.

Add items to the cart and proceed to checkout.

Fill in details and click "Place Order."

Verify that the order is stored in DynamoDB automatically! 🎉
