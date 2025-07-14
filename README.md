# 프로젝트 스켈레톤 자동화 가이드 (FastAPI + React + MySQL + Redis + Nginx + Docker)

## 📦 개요

이 프로젝트는 **풀스택 실무형 개발환경**을 "명령어 한 줄"로 자동화해서,  
**FastAPI(백엔드) + React(프론트) + MySQL + Redis + Nginx** 기반의 뼈대/설정/운영을  
누구나 빠르고 확장성 있게 시작할 수 있도록 만든 자동화 스켈레톤입니다.

---

## 🗂️ 폴더 구조 (자동 생성 예시)

project-root/
│
├─ backend/ # FastAPI 백엔드 서비스
│ ├─ app/
│ ├─ requirements.txt
│ ├─ Dockerfile.dev
│ ├─ Dockerfile.prod
│
├─ frontend/ # React 프론트엔드 서비스
│ ├─ src/
│ ├─ public/
│ ├─ package.json
│ ├─ Dockerfile.dev
│ ├─ Dockerfile.prod
│
├─ db/ # MySQL 데이터/초기화
│ ├─ data/
│ └─ init.sql
│
├─ redis/ # Redis 볼륨
│ └─ data/
│
├─ nginx/ # Nginx 설정
│ ├─ nginx.dev.conf
│ ├─ nginx.prod.conf
│ └─ Dockerfile
│
├─ docker-compose.dev.yml
├─ docker-compose.prod.yml
├─ .env.dev
├─ .env.prod
├─ .gitignore
└─ setup_skeleton.py



---

## 🚀 빠른 시작

### 1. **스켈레톤 자동 생성**
```bash
python setup_skeleton.py
2. 개발 환경 실행
bash
복사
편집
docker-compose -f docker-compose.dev.yml up --build
3. 운영(배포) 환경 실행
bash
복사
편집
docker-compose -f docker-compose.prod.yml up --build
🛠️ 자동화 진행 체크리스트
 프로젝트 뼈대/기본설정 자동 생성 (setup_skeleton.py)

 Nginx 등 설정파일 자동 생성/덮어쓰기 (generate_nginx_conf.py 등)

 도커 전체 실행/중지/초기화 스크립트 (run.sh, stop.sh, reset.sh)

 프론트/백엔드 "모듈" 자동 생성 템플릿 (add_module.py user-auth 등)

 DB 초기화/백업/복구 자동화 (db_backup.sh, db_restore.sh)

 코드 포맷/정적분석 자동화 (black, isort, eslint, prettier 등)

 CI/CD(자동 빌드/테스트/배포) 자동화 (GitHub Actions 등)

 운영 배포/롤백/스케일업 스크립트 자동화

🏁 실전 개발 플랜
 백엔드/프론트엔드 실제 개발 시작 (기능구현/실습)

 git 커밋/백업 주기적 습관화

 run.sh/stop.sh/reset.sh 등 자동화 루틴 연습

 기능별 모듈/조립식 자동화 추가(원하면)

 테스트 코드/자동화 연습(백/프론트)

 코드 포매터/정적분석 도구 적용(black, prettier 등)

 DB 백업/복구 스크립트 준비(데이터 안전)

 CI/CD 자동화 실습(깃허브 액션 yaml)

 README.md, 문서화, 실전 경험 기록

💡 팁 & 운영 주의사항
db/data, redis/data, node_modules, build 등은 항상 외부 볼륨/깃 제외!

.env 파일, .gitignore, .dockerignore 꼭 점검!

도커 볼륨 폴더만 남기면 데이터는 안전하게 보존됨

"복붙 → 엔터 한방"으로 자동화/세팅 지향

운영/개발 환경 완전 분리(도커파일, 컴포즈, 설정)

막히거나 궁금한 점은 노션/깃허브/실행스크립트/이전 기록과 함께 ChatGPT에 질문!

📝 변경/경험/문서화 기록
프로젝트 구조 및 자동화 진행 상황, 실전 경험, 문제 해결 내역 등을
README 또는 별도 노션에 지속적으로 기록/공유
(협업/버전관리, 반복 실수 방지, 성장 추적 목적)

🗂️ 참고: 주요 파일 역할
setup_skeleton.py : 전체 폴더/기본 파일/도커 설정 자동 생성

run.sh/stop.sh/reset.sh : 도커 전체 실행/중지/초기화

generate_nginx_conf.py : Nginx 등 주요 설정파일 자동화

add_module.py (예정) : 기능 모듈(예: user-auth 등) 템플릿 자동 추가

db_backup.sh/db_restore.sh (예정) : DB 백업/복구 자동화

black, prettier, isort, eslint (예정) : 코드 스타일/정적분석 자동화

GitHub Actions yaml (예정) : CI/CD 자동화

