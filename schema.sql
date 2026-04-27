DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS category;

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE enrollment (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);
