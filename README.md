# **📚 Japanese Syllabus Check AI System (SpaCy + OpenAI API)**

This application analyzes university syllabuses in Japanese using **SpaCy** for NLP parsing and **OpenAI API** for embedding-based similarity checking.

---

## **🔧 1️⃣ Installation (Windows CMD)**

### **🔹 Step 1: Clone the Repository & Set Up Virtual Environment**
```cmd
git clone https://github.com/yourusername/Syllabus_Spacy.git
cd Syllabus_Spacy
python -m venv transform
transform\Scripts\activate
pip install -r requirements.txt
```

---

## **🚀 2️⃣ Running the Application Locally**

### **🔹 Run API Server (FastAPI)**
```cmd
uvicorn main:app --reload
```
- **Access API at:** `http://127.0.0.1:8000`

### **🔹 Run Bulk Processing**
```cmd
python app/bulk_process.py --request_id sample_id
```

### **🔹 Run Individual Processing**
```cmd
python app/individual_process.py --request_id sample_id "Some text to process"
```

---

## **☁️ 3️⃣ Deploying to AWS**

### **🔹 Step 1: Push to GitHub**
```cmd
git add .
git commit -m "Updated application with SpaCy and OpenAI API"
git push origin main
```

### **🔹 Step 2: Deploy to AWS Lambda**
1. **Zip the project folder**
```cmd
cd Syllabus_Spacy
zip -r syllabus_lambda.zip *
```
2. **Upload to AWS Lambda**
   - Open **AWS Lambda** → Create Function  
   - Select **Upload from .zip file**  
   - Set **Handler** to `main.lambda_handler`  
   - Attach IAM Role **with S3 & API Gateway permissions**  

### **🔹 Step 3: Setup API Gateway**
1. Open **AWS API Gateway** → Create **New REST API**  
2. Add **/process** route → **Connect to Lambda**  
3. Deploy API → Copy **Invoke URL**  
4. Test API using:  
```cmd
curl -X POST https://your-api-url.amazonaws.com/process -d '{"request_id": "sample_id"}'
```

---

## **🛠️ 4️⃣ Deploying Using development.sh**

### **🔹 Step 1: Load Environment Variables**
```cmd
source .env.develop
```

### **🔹 Step 2: Run Deployment Script**
```cmd
sh deploy/development.sh
```

✅ This will **build, tag, push** the Docker image and **update the ECS service** with the latest version.

---

## **🎯 6️⃣ Summary of How Everything Connects**

| **File** | **Role** | **Related To** |
|----------------------------|-------------------------------------------------|--------------------------------|
| `bulk_process.py` | Runs bulk syllabus processing | Calls `text_processing.py`, `embedding_generator.py`, `s3_bucket.py`, `webhook.py` |
| `individual_process.py` | Processes single syllabus entry | Calls `embedding_generator.py` |
| `embedding_generator.py` | Generates text embeddings | Uses OpenAI API |
| `text_processing.py` | Parses Japanese text | Uses SpaCy |
| `s3_bucket.py` | Handles S3 interactions | Called by `bulk_process.py`, `individual_process.py` |
| `webhook.py` | Notifies results | Triggered after S3 upload |
| `main.py` | FastAPI entry point | Calls `syllabus_check.py` |
| `syllabus_check.py` | API endpoint handler | Calls `bulk_process.py` & `individual_process.py` |

---

## **🚀 Next Steps**
1️⃣ **Test Locally:** Run **FastAPI + processing scripts**.  
2️⃣ **Push to GitHub:** Deploy AWS Lambda & API Gateway.  
3️⃣ **Final Debugging:** Ensure Webhook & S3 work as expected.  

🔥 Now your app is fully functional, structured, and ready for production!

