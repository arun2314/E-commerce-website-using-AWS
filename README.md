# AWS-Based E-Commerce Website Deployment

This project is an e-commerce website where users can browse products, add them to the cart, and place an order. When an order is placed, the order details are stored automatically in an AWS DynamoDB table using AWS Lambda, API Gateway, and IAM roles.

## Steps to Set Up the Website

### Step 1: Create an S3 Bucket for Hosting
1. Go to **AWS S3** → Click **Create Bucket**.
2. Set a unique **Bucket Name** and **Region**.
3. Enable **Static Website Hosting** and upload `index.html`, `product.html`, and `checkout.html`.
4. Make sure the bucket policy allows public access for reading.

### Step 2: Create a DynamoDB Table for Orders
1. Go to **AWS DynamoDB** → Click **Create Table**.
2. Set **Table Name**: `Orders`.
3. Set **Primary Key**: `order_id (String)`.
4. Click **Create Table**.

### Step 3: Create an AWS Lambda Function
1. Go to **AWS Lambda** → Click **Create Function**.
2. Choose **Author from Scratch**.
3. Set **Function Name**: `StoreOrder`.
4. Choose **Runtime**: `Python 3.x`.
5. Add the required permissions:
   - `AmazonDynamoDBFullAccess`
   - `AWSLambdaBasicExecutionRole`
6. Write a Lambda function to receive data from the API Gateway and store it in DynamoDB.

### Step 4: Set Up API Gateway
1. Go to **AWS API Gateway** → Click **Create API**.
2. Choose **REST API** → Click **Build**.
3. Create a **new resource** and **new method (POST)**.
4. Integrate it with the **Lambda Function (`StoreOrder`)**.
5. Deploy the API to a **stage** (e.g., `prod`).
6. Copy the **Invoke URL** for use in the frontend.

### Step 5: Connect the Checkout Page to API Gateway
1. Update `checkout.html` to send order details to API Gateway.
2. Use JavaScript's `fetch()` method to call the API.
3. When a user clicks "Place Order," the order details are sent to the API Gateway.
4. The API Gateway triggers Lambda, which stores the order in DynamoDB.

### Step 6: Test the Setup
1. Open the website hosted on S3.
2. Add items to the cart and proceed to checkout.
3. Fill in details and click "Place Order."
4. Verify that the order is stored in **DynamoDB** automatically! 🎉


