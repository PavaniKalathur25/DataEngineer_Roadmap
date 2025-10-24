MERGE INTO target_table AS t
USING source_table AS s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.name = s.name, t.city = s.city
WHEN NOT MATCHED THEN
    INSERT (id, name, city) VALUES (s.id, s.name, s.city);
