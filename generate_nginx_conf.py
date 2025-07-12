# generate_nginx_conf.py
import os

# 필요시 True/False만 바꿔서 실행 (True: 개발, False: 운영/배포)
nginx_proxy_to_local = True  # 개발: 로컬(npm start) / 운영: 도커 컨테이너

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

def main():
    # 개발용 conf
    with open('nginx/nginx.dev.conf', 'w', encoding='utf-8') as f:
        f.write(nginx_dev_conf.lstrip('\n'))
    print('[파일 생성] nginx/nginx.dev.conf (개발모드)' if nginx_proxy_to_local else '[파일 생성] nginx/nginx.dev.conf (운영모드)')

    # 운영용 conf도 항상 갱신
    with open('nginx/nginx.prod.conf', 'w', encoding='utf-8') as f:
        f.write(nginx_prod_conf.lstrip('\n'))
    print('[파일 생성] nginx/nginx.prod.conf (운영모드)')

if __name__ == '__main__':
    main()
