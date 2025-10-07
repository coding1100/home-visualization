To run application add the below variables to your .env file

```env
ENV=dev
PROJECT_NAME=Home Visualization API
API_PREFIX=/api/v1
DATABASE_URL
SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES
STRIPE_WEBHOOK_SECRET
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY
PASSWORD_RESET_TOKEN_MINUTES
CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET
UPLOAD_TMP_DIR
UPLOAD_MAX_MB
HF_TOKEN
COMFYUI_SERVER
S3_BUCKET
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
RF_API_KEY
RF_MODEL_PROJECT
RF_MODEL_PROJECT_VERSION

```

After adding the above variables to your .env file, create and activate virtual env
For windows use the below command
```bash
py -3 -m venv .venv
. .\.venv\Scripts\Activate.ps1

```
For mac use the below command
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Create a requirements.txt file at root directory of project and run the below commands
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt

```

After adding variables abd activating the virtual env run the following command to start the application

```bash
uvicorn app.main:app --reload

```

To aply existing migrations run the below command

```bash
alembic upgrade head  
```


If any change in data-base column or table run the below command to migrate the changes

```bash
alembic revision --autogenerate -m "message"
alembic upgrade head

```

The application is containerized using docker. To build and run the docker container use the below command

```bash
docker compose up -d --build

```

Steps and commands to deploy on RunPod
1️⃣ Build the production Docker image
From your project root:
```bash
docker build -t homeviz-prod -f Dockerfile.prod .
```

2️⃣ Tag the image for Docker Hub
Replace dockerusername with your Docker Hub username if different:
```bash
docker tag homeviz-prod:latest <dockerusername>/homeviz-prod:latest
```

3️⃣ Log in to Docker Hub
```bash
docker login
```

4️⃣ Push the image to Docker Hub
```bash
docker push dockerusername/homeviz-prod:latest
```
Wait until you see:
latest: digest: sha256:xxxxxxxx... size: 856

✅ That means your image is successfully uploaded.



To Deploy on RunPod dashboard:
5️⃣ Create a new Pod Template on RunPod
Go to https://console.runpod.io

In the sidebar → My Templates → New Template
Fill in:
Type: Pod
Compute Type: CPU
Container Image: dockerusername/homeviz-prod:latest
HTTP Port: 8000
Environment Variables and values: set those accordingly
Start Command: leave blank (Dockerfile already defines CMD)
Save it as → homeviz-prod

6️⃣ Deploy the Pod
Go to Pods → Deploy
Select:
Instance: CPU → Compute-Optimized
Pod Template: homeviz-prod
Pod Name: home-visualizer-backend
Click Deploy On-Demand
7️⃣ Get the public URL

Once your pod is running, go to:
Pods → [your pod] → Connect tab
You’ll see:
Port 8000 → app

Click the “app” link or copy the URL that looks like:
https://home-visualizer-backend-8000.proxy.runpod.net

Your FastAPI backend is now live at:
https://home-visualizer-backend-8000.proxy.runpod.net/api/v1/


🔁 Redeploy after code changes

When you change code:

docker build -t homeviz-prod -f Dockerfile.prod .
docker tag homeviz-prod:latest dockrusername/homeviz-prod:latest
docker push dockerusername/homeviz-prod:latest


Then simply terminate the old pod and redeploy from the same homeviz-prod template —
RunPod will automatically pull the new image.

