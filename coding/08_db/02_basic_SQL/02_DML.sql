-- DML
-- table 사전 준비
CREATE TABLE articles (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- Insert 활용 1
-- 데이터 추가하기
INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('hello', 'world', '2000-01-01');

-- articles 테이블 전체 조회
SELECT * FROM articles;

-- Insert 활용 2
-- 여러 데이터 추가하기
INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

SELECT * FROM articles;

-- Insert 활용 3
-- 현재 시간으로 데이터 추가하기
INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('mytitle', 'mycontent', NOW());

SELECT * FROM articles;


-- Update 활용 1
-- 1번 데이터 수정하기
UPDATE 
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

SELECT * FROM articles;


-- Update 활용 2
-- 2번 데이터 수정하기
UPDATE 
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

SELECT * FROM articles;

-- Delete 활용
-- 1번 레코드 삭제
DELETE FROM 
  articles
WHERE 
  id = 1;

SELECT * FROM articles;

-- Truncate와 Delete와 비교
DELETE FROM articles;

INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('hello', 'world', '2000-01-01');

-- 아이디가 초기화 안됨
SELECT * FROM articles;

TRUNCATE articles;

INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('hello', 'world', '2000-01-01');
  
-- 아이디가 초기화 됨
SELECT * FROM articles;

