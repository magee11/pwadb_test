import boto3
import os 
from flask import request  
from app import app 


@app.route('/upload_image',methods=['POST'])
def upload_image():
    try:
        print("fkjrkf")
        image_file = request.files['file']
        raw = image_file.read()
        filename = image_file.filename
        g=upload_to_s3(filename,obj=raw)
        # 'https://'+bucketname+'.s3.'+region_name+'.amazonaws.com/'+filename)
        return f'https://{os.getenv("bucket")}.s3.{os.getenv("AWS_DEFAULT_REGION")}.amazonaws.com/{filename}'
        # return {"content":"Added successfully","error":0,"message":"success"}

    except Exception as e:
        return {"content":"Added successfully","error":str(e),"message":"success"}
def upload_to_s3(name,obj=None):
    client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"))  

    # client.upload_file(filepath, bucket, filename, ExtraArgs = {'ACL':'public-read'})
    p = client.put_object(Body=obj, Bucket=os.getenv("bucket"), Key=name , ACL = "Public-Read")

    print(p,type(p))
    return "s"
