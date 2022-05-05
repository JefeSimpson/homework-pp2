CREATE OR REPLACE FUNCTION get_phonebook_option(n integer)
  RETURNS TABLE(name VARCHAR, phone VARCHAR) 
AS
$$
#variable_conflict use_column
DECLARE
    f record;
BEGIN
    RETURN QUERY
    FOR f in select * FROM phonebook ORDER BY name limit n LOOP
    END LOOP;
END;
$$
LANGUAGE plpgsql;
