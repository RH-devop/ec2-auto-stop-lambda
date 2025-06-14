# EC2 自動停止スクリプト｜AWS Lambda + EventBridge

## 概要
このプロジェクトは、毎日決まった時間に **EC2インスタンスを自動停止** させる仕組みです。  
AWS Lambda（Python）と Amazon EventBridge を組み合わせて実現しています。

## 使用サービス
- AWS Lambda（Python 3.12）
- Amazon EC2
- Amazon EventBridge（スケジュール実行）
- IAM（LambdaにEC2操作権限付与）

## ファイル構成
- `ec2-auto-stop.py`：EC2を停止させるLambda関数
- `README.md`：この説明ファイル

## セットアップ手順
1. `ec2-auto-stop.py` の中にある `instance_id` を自分のEC2インスタンスIDに書き換える
2. AWSマネジメントコンソールからLambda関数を作成し、コードを貼り付ける
3. Lambda関数の「設定」→「アクセス権限」からIAMロールを表示し、`AmazonEC2FullAccess` ポリシーをアタッチ
4. EventBridgeで以下のようなルールを作成
   - **スケジュールパターン**：cron式（例：`cron(0 14 * * ? *)` → 日本時間23:00に毎日実行）
   - **ターゲット**：上記のLambda関数を指定

## 注意事項
- Lambdaで使用するコード内のリージョン（`region_name`）は、自分のEC2インスタンスと同じにしてください（例：東京リージョン → `ap-northeast-1`）。
- IAMロールには最低限 `stop_instances` が許可されたポリシーが必要です。
- 無料利用枠内で運用可能ですが、利用状況によっては料金が発生することがあります。
