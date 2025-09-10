-- Active: 1752638634287@@127.0.0.1@3306@db_adv
-- JOIN 사전 준비

DROP DATABASE db_adv;

CREATE DATABASE db_adv
  DEFAULT CHARACTER SET 'utf8mb4';

USE db_adv;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INTEGER,
  parent_id INTEGER,
  FOREIGN KEY (parent_id) REFERENCES users(id)
);

INSERT INTO 
  users (name, age, parent_id)
VALUES 
  ('하석주', 50, NULL),
  ('정윤미', 48, NULL),
  ('유하선', 46, NULL),
  ('하민성', 24, 1),
  ('정아인', 22, 2),
  ('송민', 19, 1),
  ('정지민', 22, 2);


CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER,
  FOREIGN KEY (userId) REFERENCES users(id)
);
INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', NULL),
  ('제목4', '내용4', 3),
  ('제목5', '내용5', 1),
  ('제목6', '내용6', NULL),
  ('제목7', '내용7', 5);

SELECT * FROM users;
SELECT * FROM articles;

-- -- JOIN 사전 준비 끝 -- 

-- INNER JOIN
-- INNER JOIN 예시
SELECT articles.*, users.id, users.name FROM articles
INNER JOIN users 
  ON users.id = articles.userId;

-- INNER JOIN은 교집합이므로, 메인 테이블이 달라져도 결과는 동일
  -- 단, 메인 테이블을 기준으로 조회하므로 조회 순서가 달라질 수 있으므로 유의
SELECT articles.*, users.id, users.name FROM users
INNER JOIN articles 
  ON users.id = articles.userId;

-- INNER JOIN 활용 1
-- 1번 회원(하석주)가 작성한 모든 게시글의 제목과 작성자명을 조회
SELECT articles.title, users.name
FROM articles
INNER JOIN users 
  ON users.id = articles.userId
WHERE users.id = 1;


-- LEFT JOIN 
SELECT articles.*, users.id, users.name FROM articles
LEFT JOIN users 
  ON users.id = articles.userId;

-- LEFT JOIN 활용 1
-- 게시글을 작성한 이력이 없는 회원 정보 조회
SELECT users.name FROM users
LEFT JOIN articles 
  ON articles.userId = users.id
WHERE articles.userId IS NULL;

-- RIGHT JOIN
SELECT articles.*, users.id, users.name FROM articles
RIGHT JOIN users 
  ON users.id = articles.userId;


-- SELF JOIN
SELECT 
  parent.id AS parent_id, 
  parent.name AS parent_name, 
  child.id AS child_id, 
  child.name AS child_name
FROM 
  users parent
INNER JOIN users child 
  ON parent.id = child.parent_id;

-- 테이블을 구분하지 않으면 Error 발생
-- SELECT 
--   users.id AS parent_id, 
--   users.name AS parent_name, 
--   users.id AS child_id, 
--   users.name AS child_name
-- FROM 
--   users
-- JOIN 
--   users ON users.id = users.parent_id;

-- SELF JOIN 활용 1
-- 서로의 형제자매가 누구인지 id와 이름 조회
SELECT 
  users.id AS user_id, 
  users.name AS user_name, 
  sibling.id AS sibling_id, 
  sibling.name AS sibling_name
FROM 
  users
JOIN 
  users sibling ON users.parent_id = sibling.parent_id
WHERE 
  users.id != sibling.id;
