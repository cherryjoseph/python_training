CREATE TABLE dept(
    deptno  NUMBER(100),
    dname   VARCHAR2(10)
);
CREATE TABLE EMP(
    empno   NUMBER(10) PRIMARY KEY ,
    ename   VARCHAR2(10) NOT NULL
);
INSERT INTO dept(deptno ,dname)
    VALUES (1,'Sales');

INSERT INTO dept(deptno ,dname)
    VALUES (2,'Marketing');
INSERT INTO EMP(empno ,ename)
    VALUES(100 , 'cheriyan');

INSERT INTO EMP(empno ,ename)
    VALUES(101 , 'joseph');
BEGIN
    DBMS_UTILITY.compile_schema
        schema => 'SCOTT', 
        compile_all => false
    );
END;    
