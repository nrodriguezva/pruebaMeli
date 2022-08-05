DROP TABLE IF EXISTS frequency_word
DROP TABLE IF EXISTS archivo
CREATE TABLE public.archivo (
	id SERIAL PRIMARY KEY,
	data_file bytea NOT NULL,
	name_file CHARACTER VARYING(255)  NOT NULL,
	extension_file CHARACTER VARYING(255)  NOT NULL
);
CREATE TABLE public.frequency_word (
	id SERIAL PRIMARY key,
	id_file INTEGER NOT NULL,
	word CHARACTER VARYING(255)  NOT NULL,
	frequency NUMERIC NOT NULL,
	FOREIGN KEY(id_file) REFERENCES archivo(id)
);

