import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('orders')  # Ensure this matches your DynamoDB table name

def lambda_handler(event, context):
    try:
        data = json.loads(event["body"])

        order_id = str(uuid.uuid4())

        order_item = {
            "order_id": order_id,
            "name": data["name"],
            "phone": data["phone"],
            "email": data["email"],
            "address": data["address"],
            "paymentMethod": data["paymentMethod"],
            "products": data["products"],  # Store product details
            "totalAmount": data["totalAmount"],  # Store total amount
            "orderDate": str(datetime.utcnow())  # Store order date
        }
        
        table.put_item(Item=order_item)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Order placed successfully!", "order_id": order_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error placing order", "error": str(e)})
        }
