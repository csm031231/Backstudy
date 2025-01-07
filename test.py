import psycopg2

# 데이터베이스 연결 설정
DB_CONFIG = {
    "host": "localhost",   # PostgreSQL 서버 주소
    "database": "abc",  # 데이터베이스 이름
    "user": "postgers",    # 사용자 이름
    "password": "1231" # 비밀번호
}

try:
    connection = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="testuser",
        options="-c client_encoding=UTF8"  # 인코딩 명시
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(cursor.fetchone())
    cursor.close()
    connection.close()
except Exception as e:
    print("오류 발생:", e)
