SET timezone = 'Europe/London';
\connect notes_project_data;

DROP TABLE IF EXISTS test CASCADE;
CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    num INTEGER,
    txt varchar(10)
);
INSERT INTO test(num, txt) VALUES (6, 'foo');
INSERT INTO test(num, txt) VALUES (9, 'bar');

CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    data TIMESTAMPTZ NOT NULL,
    txt TEXT NOT NULL
);
