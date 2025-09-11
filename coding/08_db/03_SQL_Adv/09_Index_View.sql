USE world;

-- DROP INDEX code_idx ON city;

-- Index 생성하기
CREATE TABLE table_name (
  column1 INT PRIMARY KEY AUTO_INCREMENT,
  column2 VARCHAR(150) DEFAULT NULL,
  column3 VARCHAR(30),
  -- 생성하기 1 (INDEX 키워드 사용)
  INDEX index_name (column2),
  -- 생성하기 2 (KEY 키워드 사용)
  KEY index_name2 (column3)
);

-- index 추가하기 1
CREATE INDEX index_name
ON table_name (column1, column2, ...);

-- index 추가하기 2
ALTER TABLE table_name
ADD INDEX index_name (column1, column2, ...);



SHOW CREATE TABLE city;

-- CREATE TABLE `city` (
--   `ID` int NOT NULL AUTO_INCREMENT,
--   `Name` char(35) NOT NULL DEFAULT '',
--   `CountryCode` char(3) NOT NULL DEFAULT '',
--   `District` char(20) NOT NULL DEFAULT '',
--   `Population` int NOT NULL DEFAULT '0',
--   PRIMARY KEY (`ID`),
--   KEY `CountryCode` (`CountryCode`),
--   KEY `idx_city_name` (`Name`),
--   CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=4080 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


-- index 사용하기 1
-- 일반 조회시 활용
SELECT * FROM city
WHERE Name = 'Seoul';

-- index 사용하기 2
-- 정렬시 활용
SELECT * FROM city
ORDER BY Name;

-- index 사용하기 3
-- JOIN 시 활용
SELECT city.Name, country.Name 
FROM city
JOIN country ON city.CountryCode = country.Code
WHERE city.Name = 'Seoul';


-- index 삭제하기 1
ALTER TABLE table_name
DROP INDEX index_name;

-- index 삭제하기 2
DROP INDEX index_name
ON table_name;


----------------------------------------------
---- View

-- View 활용 1
-- 국가 코드와 이름을 v_simple_country라는 이름의 view로 생성
CREATE VIEW v_simple_country AS
SELECT Code, Name
FROM country;

SELECT *
FROM v_simple_country;

---
DROP VIEW v_simple_country;

-- View 활용 2
-- 각 국가별 가장 인구가 많은 도시를 조인한 뷰를 v_largest_city_per_country 라는 이름의 view로 생성
CREATE VIEW v_largest_city_per_country AS
SELECT 
  c.Name AS CountryName, 
  ci.Name AS LargestCity, 
  ci.Population AS CityPopulation,
  c.Population AS CountryPopulation
FROM country c
JOIN city ci ON c.Code = ci.CountryCode
WHERE (ci.CountryCode, ci.Population) IN (
    SELECT CountryCode, MAX(Population)
    FROM city
    GROUP BY CountryCode
);

SELECT * FROM V_largest_city_per_country;

-- 생성한 View 활용
-- v_largest_city_per_country 뷰를 이용하여 Asia 국가 중 가장 인구가 
-- 작은 곳 보다 인구가 많은 모든 도시의 개수를 조회
SELECT COUNT(*) AS CountCity
FROM v_largest_city_per_country
WHERE CityPopulation >= (
  SELECT MIN(Population)
  FROM country
  GROUP BY Continent
  HAVING Continent = 'Asia'
);

DROP VIEW v_largest_city_per_country;
