USE world; 

-- Single-row Subquery
-- 'North America' 대륙의 평균 인구
SELECT AVG(Population) FROM country WHERE Continent = 'North America';

-- 'North America' 대륙의 평균 인구보다 인구가 많은 국가의 이름과 인구 조회
SELECT 
  Name, Population
FROM 
  country
WHERE 
  Population > (
    SELECT AVG(Population) 
    FROM country
    WHERE Continent = 'North America'
  );


-- 단일행이 아닐 때 에러 발생

-- SELECT 
--   Name, Population
-- FROM 
--   country
-- WHERE 
--   Population > (
--     SELECT Population
--     FROM country
--     WHERE Continent = 'North America'
--   );



-- Single-row Subquery
-- country 테이블의 ‘Benin’ 이라는 국가의 국가 코드
SELECT Code FROM country WHERE Name = 'Benin';

-- country 테이블의 ‘Benin’ 이라는 국가의 국가 코드를 이용하여, city 테이블에 등록된 ‘Benin’의 모든 도시 정보를 조회
SELECT
  * 
FROM 
  city
WHERE 
  CountryCode = (
    SELECT Code FROM country WHERE Name = 'Benin'
  );


-- Single-row Subquery
-- 아래 쿼리는 country 정보를 얻을 수 없으므로 실행 불가
-- SELECT AVG(city.Population) FROM city WHERE city.CountryCode = country.Code;


-- country 테이블의 각 국가 마다 해당 국가 소속의 평균 도시 인구를 ​city 테이블을 이용하여 조회​
-- 메인 쿼리의 country 테이블 정보를 활용하여
  -- 서브 퀴리에서 필요 정보 집계하여 평균 값 1개를 반환
SELECT 
  country.Name AS CountryName,
  (
    SELECT AVG(city.Population) 
    FROM city 
    WHERE city.CountryCode = country.Code
  ) AS AvgCityPopulation
FROM country;

--------------------------------------------------



-- multi-row subquery
-- 대륙 정보가 Asia인 국가의 코드
SELECT Code FROM country WHERE Continent = 'Asia';

-- Asia 에 소속된 모든 도시를 조회
SELECT * 
FROM city
WHERE 
  CountryCode IN (
    SELECT Code
    FROM country
    WHERE Continent = 'Asia'
  )

-- multi-row subquery
-- 인구가 10,000,000명 이상인 국가들의 국가 코드
SELECT Code FROM country WHERE Population >= 10000000;

-- 인구가 10,000,000명 이상인 국가들의 국가 코드, 도시 이름, 지구, 인구를 조회
SELECT co.Code, c.Name, c.District, c.Population
FROM 
  city c
  JOIN (SELECT Code
        FROM country
        WHERE Population >= 10000000) co
ON c.CountryCode = co.Code;

--------------------




-- multi-column subquery
-- 각 대륙별 독립 연도
SELECT Continent, MAX(IndepYear)
FROM country
GROUP BY Continent;

-- 각 대륙별 독립 연도가 최근인 국가의 이름, 대륙, 독립 연도를 조회
SELECT 
  Name, Continent, IndepYear
FROM country
WHERE (Continent, IndepYear) IN (
    SELECT Continent, MAX(IndepYear)
    FROM country
    GROUP BY Continent
);


-- multi-column subquery
-- Africa에서 가장 땅이 넓은 국가의 이름, 대륙, 면적을 조회
SELECT 
  Name, Continent, SurfaceArea
FROM country
WHERE (Continent, SurfaceArea) = (
    SELECT Continent, MAX(SurfaceArea)
    FROM country
    GROUP BY Continent
    HAVING Continent = 'Africa'
);
