CREATE OR REPLACE PROCEDURE add_new_phonebooks(
    list_new_phonebooks varchar[ (11) ]
)
AS $$

BEGIN
    INSERT INTO phonebook(name, phone)
    FOR new_name, new_phone in list_new_phonebooks LOOP
    VALUES(new_name, new_phone)
    END LOOP;
END;
LANGUAGE plpgsql;

