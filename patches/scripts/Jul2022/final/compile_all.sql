BEGIN
    DBMS_UTILITY.compile_schema
        schema => 'SCOTT', 
        compile_all => false
    );
END;    