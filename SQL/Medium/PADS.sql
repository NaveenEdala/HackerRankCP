SELECT NAME||'('||SUBSTR(Occupation,1,1)||')' FROM OCCUPATIONS ORDER BY NAME;
SELECT 'There are a total of '||COUNT(Occupation)||' '||LOWER(Occupation)||'s.' FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(Occupation),Occupation;
