/* 1 */
SELECT customer.first_name AS first_name, customer.last_name AS last_name, email, address, city.city_id, city
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312;

/*2*/
SELECT film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre
FROM film
JOIN  film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id;

/* 3 */
SELECT film.title AS title, film.description AS description, film.release_year AS release_year, actor.first_name AS actor_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

/* 4 */
SELECT store.store_id, city.city_id, customer.first_name AS first_name, customer.last_name AS last_name, customer.email AS email, address.address AS address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN store ON customer.store_id = store.store_id
WHERE store.store_id = 1 AND (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459);

/* 5 */
SELECT film.title AS title, film.description AS description, film.release_year AS release_year, film.rating, film.special_features AS special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE '%behind the%';

/* 6 */
SELECT actor.first_name AS first_name, actor.last_name AS last_name, actor.last_update AS last_update
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

/* 7 */
SELECT film.film_id, film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre, payment.amount AS rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
WHERE payment.amount = 2.99 AND  category.name LIKE '%drama%'
ORDER BY title ASC;

/* 8 */
SELECT actor.actor_id, film.film_id, film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre, CONCAT(" ", actor.first_name, ' ', actor.last_name) AS full_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER';