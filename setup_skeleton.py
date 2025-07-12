import os

# 개발할 때 프론트엔드를 로컬(npm start)로 돌릴지, 도커로 돌릴지 선택
nginx_proxy_to_local = True   # True: host.docker.internal (로컬), False: frontend 컨테이너

folders = [
    'backend/app',
    'db/data',
    'redis/data',
    'nginx'
]

nginx_dev_conf = f"""
server {{
    listen 80;
    location /api/ {{
        proxy_pass http://backend:8000/;
    }}
    location / {{
        proxy_pass http://{'host.docker.internal:3000' if nginx_proxy_to_local else 'frontend:3000'};
    }}
}}
"""

nginx_prod_conf = """
server {
    listen 80;
    location /api/ {
        proxy_pass http://backend:8000/;
    }
    location / {
        proxy_pass http://frontend:80;
    }
}
"""

files = {
    '.gitignore': """
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Node/React
node_modules/
build/
dist/
npm-debug.log
yarn-debug.log
yarn-error.log

# OS/IDE
.DS_Store
Thumbs.db
.vscode/
.idea/
*.swp

# 환경변수/비밀정보
.env
.env.*
*.env

# 도커 데이터/볼륨
db/data/
redis/data/
""",
    '.dockerignore': """
node_modules
build
dist
.git
.gitignore
.env
.env.*
db/data
redis/data
__pycache__/
*.pyc
*.pyo
*.log
.vscode
.idea
README.md
*.md
Dockerfile
""",
    # backend
    'backend/requirements.txt': "fastapi\nuvicorn\n",
    'backend/app/main.py': """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI!"}
""",
    'backend/Dockerfile.dev': """
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
""",
    'backend/Dockerfile.prod': """
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
""",
    # db
    'db/init.sql': """
CREATE DATABASE IF NOT EXISTS sampledb;
USE sampledb;
CREATE TABLE IF NOT EXISTS hello (
    id INT PRIMARY KEY AUTO_INCREMENT,
    msg VARCHAR(100)
);
INSERT INTO hello (msg) VALUES ('Hello from MySQL!');
""",
    # nginx
    'nginx/nginx.dev.conf': nginx_dev_conf,
    'nginx/nginx.prod.conf': nginx_prod_conf,
    'nginx/Dockerfile': """
FROM nginx:alpine
COPY nginx.dev.conf /etc/nginx/conf.d/default.conf
""",
    # docker-compose (db 호스트포트 13306, 필요시 수정)
    'docker-compose.dev.yml': """
version: "3.9"
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    volumes:
      - ./backend/app:/app/app
    env_file:
      - .env.dev
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  db:
    image: mysql:8
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: sampledb
    volumes:
      - ./db/data:/var/lib/mysql
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "13306:3306"

  redis:
    image: redis:7
    restart: always
    volumes:
      - ./redis/data:/data
    ports:
      - "6379:6379"

  nginx:
    build:
      context: ./nginx
      dockerfile: Dockerfile
    ports:
      - "80:80"
    depends_on:
      - backend
""",
    'docker-compose.prod.yml': "",
    '.env.dev': "EXAMPLE_KEY=dev\n",
    '.env.prod': "EXAMPLE_KEY=prod\n",
    'README.md': "# 프로젝트 스켈레톤 자동 생성 예시\n"
}

def make_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f'[폴더 생성] {folder}')

def make_files():
    for filepath, content in files.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.lstrip('\n'))
        print(f'[파일 생성] {filepath}')

if __name__ == '__main__':
    make_folders()
    make_files()
    print("\n✅ 폴더/파일/코드 자동 생성 완료! (.gitignore, .dockerignore, 볼륨경로, nginx 프록시 설정 모두 포함)")
    print("프론트엔드는 npx create-react-app frontend로 따로 설치, 도커는 db/redis/nginx/백엔드만 관리")
    print(f"nginx 프록시 설정: {'로컬 npm start' if nginx_proxy_to_local else '도커 frontend 컨테이너'}")
