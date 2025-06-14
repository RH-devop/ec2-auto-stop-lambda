import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-northeast-1')  # 東京リージョン
    instance_id = 'i-xxxxxxxxxxx'  # あなたのEC2インスタンスIDに置き換え

    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print("停止要求を送信しました:", response)
    except Exception as e:
        print("エラー:", e)
