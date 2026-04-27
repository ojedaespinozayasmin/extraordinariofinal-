-- Categorías
INSERT INTO category (name) VALUES ('Programming');
INSERT INTO category (name) VALUES ('Data Science');

-- Cursos (10)
INSERT INTO course (name, category_id) VALUES ('Python Basics', 1);
INSERT INTO course (name, category_id) VALUES ('Flask API', 1);
INSERT INTO course (name, category_id) VALUES ('Django', 1);
INSERT INTO course (name, category_id) VALUES ('JavaScript', 1);
INSERT INTO course (name, category_id) VALUES ('React', 1);
INSERT INTO course (name, category_id) VALUES ('Machine Learning', 2);
INSERT INTO course (name, category_id) VALUES ('Pandas', 2);
INSERT INTO course (name, category_id) VALUES ('Data Viz', 2);
INSERT INTO course (name, category_id) VALUES ('Statistics', 2);
INSERT INTO course (name, category_id) VALUES ('SQL for Data', 2);

-- Alumnos (10)
INSERT INTO student (name) VALUES ('Ana García');
INSERT INTO student (name) VALUES ('Luis Martínez');
INSERT INTO student (name) VALUES ('Carla Rodríguez');
INSERT INTO student (name) VALUES ('Jorge López');
INSERT INTO student (name) VALUES ('María Fernández');
INSERT INTO student (name) VALUES ('Carlos Sánchez');
INSERT INTO student (name) VALUES ('Laura Gómez');
INSERT INTO student (name) VALUES ('Pedro Díaz');
INSERT INTO student (name) VALUES ('Sofía Ruiz');
INSERT INTO student (name) VALUES ('Diego Torres');

-- Inscripciones
INSERT INTO enrollment VALUES (1,1),(1,2),(1,6);
INSERT INTO enrollment VALUES (2,2),(2,3),(2,7);
INSERT INTO enrollment VALUES (3,1),(3,4),(3,8);
INSERT INTO enrollment VALUES (4,5),(4,9);
INSERT INTO enrollment VALUES (5,6),(5,10);
INSERT INTO enrollment VALUES (6,2),(6,7);
INSERT INTO enrollment VALUES (7,3),(7,8),(7,1);
INSERT INTO enrollment VALUES (8,4),(8,9);
INSERT INTO enrollment VALUES (9,5),(9,10);
INSERT INTO enrollment VALUES (10,1),(10,2),(10,6);
