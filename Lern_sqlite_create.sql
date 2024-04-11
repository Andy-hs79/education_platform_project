CREATE TABLE User (
	id integer,
	ferst_name string,
	last_name string,
	login string,
	password string
);

CREATE TABLE Teacher (
	id integer,
	id_user integer,
	first_name string,
	last_name string
);

CREATE TABLE Group (
	id integer,
	id_cours integer,
	id_teacher integer,
	name string
);

CREATE TABLE Тест (
	id integer,
	Test string,
	name string,
	description string,
	index_number integer,
	time_limit float,
	creator_id integer
);

CREATE TABLE Questions (
	id integer,
	id_test integer,
	answer_type_id integer,
	index_number integer
);

CREATE TABLE Answer_options (
	id integer,
	id_question integer,
	answer string,
	bool boolean
);

CREATE TABLE Answer_type (
	id integer,
	name string
);

CREATE TABLE Requered_test (
	id integer,
	id_test integer,
	id_requered integer
);

CREATE TABLE Requered_article (
	id integer,
	id_test integer,
	id_requered integer
);

CREATE TABLE Topic (
	id integer,
	name string,
	description text,
	id_course string,
	index_number integer
);

CREATE TABLE Course (
	id integer PRIMARY KEY AUTOINCREMENT,
	name string PRIMARY KEY AUTOINCREMENT,
	id_creator integer PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Course_tearcher (
	id integer PRIMARY KEY AUTOINCREMENT,
	id_course integer,
	id_teacher integer
);

CREATE TABLE group_student (
	id integer,
	id_student integer,
	id_group integer
);

CREATE TABLE student (
	id integer,
	id_user integer
);

CREATE TABLE "Completed test" (
	id integer PRIMARY KEY AUTOINCREMENT,
	id_user integer PRIMARY KEY AUTOINCREMENT,
	id_test integer PRIMARY KEY AUTOINCREMENT,
	bool boolean PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "Completed article" (
	id binary PRIMARY KEY AUTOINCREMENT,
	id_user binary PRIMARY KEY AUTOINCREMENT,
	id_article binary PRIMARY KEY AUTOINCREMENT,
	is_completed binary PRIMARY KEY AUTOINCREMENT
);

















