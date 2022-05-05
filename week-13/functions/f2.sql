CREATE OR REPLACE PROCEDURE add_new_phonebook(
    new_name varchar,
    new_phone varchar
)
AS $$

BEGIN
    INSERT INTO phonebook(name, phone) 
    VALUES(new_name, new_phone);

END; 
$$
LANGUAGE plpgsql;