-- RIGHT, LEFT JOIN 헷갈렸음
-- 어떤 데이터를 다 보고 싶은지에 따라!!
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I
RIGHT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;
