-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO f
INNER JOIN FISH_NAME_INFO fn ON f.FISH_TYPE = fn.FISH_TYPE
WHERE fn.FISH_NAME IN ('BASS','SNAPPER')