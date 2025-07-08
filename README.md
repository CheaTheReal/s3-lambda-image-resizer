# 🖼️ AWS Lambda S3 Image Resizer

This project automatically resizes uploaded images using AWS Lambda, triggered by S3 events, and delivers optimized images globally via CloudFront.

## ✅ What It Does

- Accepts image uploads to an S3 bucket (`chea-image-source`)
- Triggers a Lambda function written in Python using Pillow
- Resizes images to 128x128
- Saves resized versions to another S3 bucket (`chea-image-resized`)
- Delivers them globally via CloudFront CDN

---

## 🛠️ Services Used

- **Amazon S3** – Object storage for original and resized images
- **AWS Lambda** – Serverless function to process and resize
- **IAM** – Role-based access for secure permissions
- **CloudWatch Logs** – For debugging Lambda
- **CloudFront** – Fast, global delivery of resized images
- **AWS CloudShell** – Used to package native Python dependencies

---

## 🔍 Architecture

```text
[User Uploads Image]
         |
         v
+------------------+
|  S3 Source Bucket|
| chea-image-source|
+------------------+
         |
         v (Trigger)
+------------------+
|    Lambda (PIL)  |
|   Resizes Image  |
+------------------+
         |
         v
+---------------------+
| S3 Resized Bucket   |
| chea-image-resized  |
+---------------------+
         |
         v
+------------------------------+
| CloudFront Distribution      |
| Public global image access   |
+------------------------------+

