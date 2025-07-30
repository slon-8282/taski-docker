FROM node:18
WORKDIR /app

# 1. Копируем только файлы зависимостей
COPY package.json package-lock.json ./

# 2. Устанавливаем зависимости с явным указанием версии react-scripts
RUN npm install --legacy-peer-deps
RUN npm install react-scripts@5.0.1 --save-exact

# 3. Проверяем установку
RUN ls -la node_modules/.bin/react-scripts

# 4. Копируем остальные файлы
COPY . .

# 5. Собираем проект
RUN npm run build

# 6. Копируем сборку в volume
RUN mkdir -p /frontend_static && cp -r build/. /frontend_static/

CMD ["npm", "start"]