import os

# 폴더 구조 정의
folders = [
    'backend/app',
    'frontend/src',
    'frontend/public',
    'db/data',
    'redis/data',
    'nginx'
]

# 파일(경로, 내용) 정의
files = {
    '.gitignore': """
# Python
__pycache__/
*.pyc

# Node
node_modules/
build/

# Docker data
db/data/
redis/data/

# Env
.env*
""",
    'backend/requirements.txt': "fastapi\nuvicorn\n",
    'backend/Dockerfile.dev': "# 개발용 Dockerfile (FastAPI)\n",
    'backend/Dockerfile.prod': "# 운영용 Dockerfile (FastAPI)\n",
    'frontend/package.json': "{\n  \"name\": \"frontend\"\n}\n",
    'frontend/Dockerfile.dev': "# 개발용 Dockerfile (React)\n",
    'frontend/Dockerfile.prod': "# 운영용 Dockerfile (React)\n",
    'db/init.sql': "-- MySQL 초기 데이터\n",
    'nginx/nginx.dev.conf': "# 개발용 Nginx conf\n",
    'nginx/nginx.prod.conf': "# 운영용 Nginx conf\n",
    'nginx/Dockerfile': "# Nginx Dockerfile\n",
    'docker-compose.dev.yml': "# 개발용 docker-compose\n",
    'docker-compose.prod.yml': "# 운영용 docker-compose\n",
    '.env.dev': "# 개발환경 변수\n",
    '.env.prod': "# 운영환경 변수\n",
    'README.md': "# 프로젝트 뼈대 자동 생성 예시\n"
}

def make_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f'[폴더 생성] {folder}')

def make_files():
    for filepath, content in files.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[파일 생성] {filepath}')

if __name__ == '__main__':
    make_folders()
    make_files()
    print("\n✅ 기본 폴더/파일 자동 생성 완료!")
    print("이제 각 파일/폴더에 실제 코드를 추가해가며 개발하면 됩니다.")