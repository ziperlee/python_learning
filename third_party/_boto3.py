"""
 Created by liwei on 2019/12/13.
"""
# s3 boto3文档
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client


import boto3

BUCKET = "ai_vision"
aws_access_key_id = "8KNQVOU27LTFQ32LD3DT"
aws_secret_access_key = "VZM9KfGqFn6Q6DeYKY8wsR10l1K1DPWu8W4YA0JM"

s3 = boto3.client(
    service_name="s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    endpoint_url="http://s3.td:8080",
)

# 桶内文件
# objects = s3.list_objects(Bucket=BUCKET)['Contents']
# for object in objects:
#     print(object.get('Key'))

# 指定目录内文件
objects = s3.list_objects(Bucket=BUCKET, Prefix='ai-face-gen/v1-0-1-20191212/models')['Contents']
for object in objects:
    file_name = object.get('Key')
    print(object.get('Key'))
    # if file_name != 'ai-face-gen/v1-0-1-20191212/':
    #     print(object.get('Key'))
    #     s3.download_file(BUCKET, file_name, '/Users/zipee/code/python_learning/hh/'+file_name.split('/')[-1])

# 创建桶
# s3.create_bucket(Bucket="ai_vision")

# 查看所有桶
# buckets = s3.list_buckets()["Buckets"]
# for bucket in buckets:
#     print(bucket.get("Name"))


# 删除桶
# 桶内对象必须全被删除
# try:
#     s3.delete_bucket(Bucket="ai-vision")
# except Exception as e:
#     print(e)

# 删除文件
# s3.delete_object(Bucket='ai-vision', Key='contentsecurity/terror.model.encrypted')
# s3.delete_object(Bucket='ai-vision', Key='contentsecurity/terror_finetune_resnet50_v5.15')

# # 上传文件
# s3.upload_file('./test.py', 'test_lw', 'contentsecurity/ai-face-gen/test.py')
#
# # 下载文件
# s3.download_file(BUCKET, 'contentsecurity/terror_finetune_resnet50_v5.15',
#                  'terror_finetune_resnet50_v5.15')
