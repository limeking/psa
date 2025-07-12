import os

frontend_dockerfiles = {
    'frontend/Dockerfile.dev': """
FROM node:20
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
CMD ["npm", "start"]
""",
    'frontend/Dockerfile.prod': """
FROM node:20 as build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""
}

def make_files(files):
    for filepath, content in files.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.lstrip('\n'))
        print(f'[파일 생성] {filepath}')

if __name__ == '__main__':
    make_files(frontend_dockerfiles)
    print("\n✅ 프론트엔드 도커파일(Dockerfile.dev, Dockerfile.prod) 자동 생성 완료!")
