WITH RECURSIVE numbers(n) AS (
    VALUES (1)
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 100
), words AS (
    SELECT n,
        CASE WHEN n % 3 = 0 THEN 'Fizz' ELSE '' END
        || CASE WHEN n % 5 = 0 THEN 'Buzz' ELSE '' END
        AS word
    FROM numbers
)
SELECT COALESCE(NULLIF(word, ''), CAST(n AS TEXT))
FROM words
ORDER BY n;
