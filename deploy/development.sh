#!/bin/sh

# 環境変数の読み込み (デフォルトは .env.develop)
ENV_FILE="${ENV_FILE:-.env.develop}"
if [ -f "$ENV_FILE" ]; then
  source "$ENV_FILE"
else
  echo "Error: Environment file $ENV_FILE not found"
  exit 1
fi

# 必要な環境変数のチェック
REQUIRED_VARS=("AWS_PROFILE" "AWS_REGION" "AWS_ACCOUNT_ID" "ECS_CLUSTER" "ECS_SERVICE" "ECR_REPOSITORY" "IMAGE_NAME" "IMAGE_ENV")
for var in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: Required environment variable $var is not set"
    exit 1
  fi
done

# 現在の desired count を取得
DESIREDCOUNT=$(aws ecs --profile "$AWS_PROFILE" describe-services --cluster "$ECS_CLUSTER" --services "$ECS_SERVICE" | jq -r '.services[].desiredCount')

echo '-----------------------'
echo "Desired Count: ${DESIREDCOUNT}"
echo '-----------------------'

# ECR 認証 & Docker ビルド・プッシュ
echo "Logging in to Amazon ECR..."
aws ecr --profile "$AWS_PROFILE" get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

if [ $? -ne 0 ]; then
  echo "Error: ECR login failed"
  exit 1
fi

echo "Building Docker image..."
docker build --platform linux/amd64 -t "$IMAGE_NAME":"$IMAGE_ENV" .

if [ $? -ne 0 ]; then
  echo "Error: Docker build failed"
  exit 1
fi

echo "Tagging and pushing Docker image..."
DOCKER_TAG="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_ENV"
docker tag "$IMAGE_NAME":"$IMAGE_ENV" "$DOCKER_TAG"
docker push "$DOCKER_TAG"

if [ $? -ne 0 ]; then
  echo "Error: Docker push failed"
  exit 1
fi

echo "Updating ECS service..."
aws ecs --profile "$AWS_PROFILE" update-service --cluster "$ECS_CLUSTER" --service "$ECS_SERVICE" --desired-count "$DESIREDCOUNT" --force-new-deployment

if [ $? -ne 0 ]; then
  echo "Error: ECS update service failed"
  exit 1
fi

echo "Deployment successful!"