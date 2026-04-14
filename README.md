# AWS × Django Webアプリ構成（ポートフォリオ）

## ■ 概要

本プロジェクトは、AWS上にDjangoアプリケーションの本番環境を構築し、
ALBおよびAuto Scalingを用いたスケーラブルな構成の理解を目的として作成しました。

---

## ■ 構成図

![AWS構成図](https://github.com/user-attachments/assets/1f0ddafc-8edd-4493-93c5-5cb3508c1990)

本構成は、可用性とセキュリティを考慮し、ALB・Auto Scaling・Private Subnet構成を採用しています。

※コスト最適化のためNAT Gatewayは未使用としています


---

## ■ 使用技術

### 【インフラ】

* AWS（VPC / EC2 / RDS / S3 / ALB / CloudWatch / SNS / Auto Scaling）
* Linux（Amazon Linux）
* Nginx
* Gunicorn

### 【アプリケーション】

* Python（Django）
* MySQL（RDS）

### 【その他】

* Git / GitHub

---

## ■ アーキテクチャ構成

### ● ネットワーク

* VPC内にPublic / Private Subnetを分離
* Public Subnet：EC2（Webサーバ）
* Private Subnet：RDS（MySQL）

### ● Webサーバ

* EC2上にDjangoアプリを配置
* Nginx + Gunicornでアプリケーションを配信

### ● データベース

* RDS（MySQL）をPrivate Subnetに配置
* 外部から直接アクセス不可としセキュリティを確保

### ● ストレージ

* S3に静的ファイルを配置

### ● 負荷分散・可用性

* ALB（Application Load Balancer）を使用
* Auto Scalingにより負荷に応じてEC2をスケール

### ● 監視・通知

* CloudWatchでリソース監視
* SNSでアラートをメール通知

---

## ■ 工夫した点
- ALBを用いた負荷分散構成を実装
- Auto Scalingにより負荷に応じたスケーリングを実現
- セキュリティグループを分離し、ALB経由のみアクセス可能に設計
- 静的ファイルをS3に分離し、Webサーバの負荷軽減

## ■ 苦労した点
- ALBのターゲットグループにおけるヘルスチェック設定（HTTPステータスコードの理解）
- セキュリティグループ間の通信制御による疎通不良の切り分け
- NginxとGunicornのリバースプロキシ構成の理解

## ■ 今後の改善点

* NAT Gateway導入によるPrivate環境の外部通信最適化
* CI/CD（GitHub Actionsなど）の導入
* HTTPS対応（ACM + ALB）

---

## ■ 学んだこと

* AWSにおける基本的なインフラ構成の理解
* Webアプリケーションの本番運用構成
* 障害監視および通知設計の重要性

---

## ■ URL
- GitHub：
  https://github.com/tomonoriOkabe0509/django-app-test

- アプリケーション：
  http://test-alb-614651923.ap-northeast-1.elb.amazonaws.com

---

## ■ 補足

※本構成は学習目的で構築しており、一部コスト最適化のため簡略化している部分があります。
