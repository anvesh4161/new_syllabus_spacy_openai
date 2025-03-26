import os

class Settings:
    AWS_PROFILE = os.getenv("AWS_PROFILE", "syllabus-check")
    AWS_REGION = os.getenv("AWS_REGION", "ap-northeast-1")
    ECS_CLUSTER = os.getenv("ECS_CLUSTER", "syllabus-check-development-individual-cluster")
    ECS_SERVICE = os.getenv("ECS_SERVICE", "individual")
    ECR_REPOSITORY = os.getenv("ECR_REPOSITORY", "syllabus-check-ai")
    IMAGE_NAME = os.getenv("IMAGE_NAME", "syllabus-check-ai")
    IMAGE_ENV = os.getenv("IMAGE_ENV", "development")

settings = Settings()