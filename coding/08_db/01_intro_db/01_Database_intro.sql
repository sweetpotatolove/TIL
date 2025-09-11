-- Active: 1752638634287@@127.0.0.1@3306@mysql
-- CREATE DATABASE
CREATE DATABASE db_intro
    DEFAULT CHARACTER SET = 'utf8mb4';

USE db_intro;

-- DDL CREATE
-- 테이블 생성하기
CREATE TABLE examples (
  ExamId INT PRIMARY KEY AUTO_INCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

-- Table 스키마 확인 1
DESCRIBE examples;
-- Table 스키마 확인 2
SHOW CREATE TABLE examples;

-- 제약 조건 정의하여 테이블 생성하기
CREATE TABLE users (
    userid INT PRIMARY KEY AUTO_INCREMENT,
    examid INT,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age >= 0 AND age <= 150),
    balance INT DEFAULT 0, 
    FOREIGN KEY (examid) REFERENCES examples(examid),
    CHECK (balance >= -5000 AND balance <= 5000),
    CONSTRAINT unique_email UNIQUE (email),
    CONSTRAINT valid_email CHECK (email LIKE '%_@__%.__%')
);

DESCRIBE users;
SHOW CREATE TABLE users;

-- 테이블 수정하기

-- Add Column 1
ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

-- Add Column 2
ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL DEFAULT 0,
ADD COLUMN Address VARCHAR(100) NOT NULL DEFAULT 'default value';

-- Rename Column
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;

-- Rename Table
ALTER TABLE examples
RENAME TO new_examples;


-- 테이블 삭제하기
DROP TABLE new_examples;

-- users 테이블 먼저 삭제
DROP TABLE users;
-- new_examples 테이블 삭제
DROP TABLE new_examples;


-- 테이블 데이터 비우기
-- 데이터를 넣는 것을 아직 진도가 나가지 않아 실습은 다음 수업에서 진행
-- TRUNCATE TABLE new_examples;