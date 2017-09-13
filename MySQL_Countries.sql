/*MySQL Countries #1 */
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

/*MySQL Countries #2 */
SELECT countries.name AS country_name, COUNT(cities.id) AS city_count
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY country_id
ORDER BY city_count DESC;

/*MySQL Countries #3 */
SELECT cities.name AS city_name, cities.population AS population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000;

/* #4 */
SELECT countries.name AS country_name, languages.language AS languages, languages.percentage AS percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

/* #5 */
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

/* #6 */
SELECT name, government_form, life_expectancy
FROM countries
WHERE  government_form LIKE '%Constitutional Monarchy%' AND capital > 200 AND life_expectancy > 75;

/* #7 */
SELECT countries.name AS country_name, cities.name AS city_name, district, cities.population AS population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;

/* #8 */
SELECT region, COUNT(id) AS country_count
FROM countries
GROUP BY region
ORDER BY country_count DESC