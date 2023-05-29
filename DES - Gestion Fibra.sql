-- ODF


create table FOODF (
	id serial primary key,
	codigo varchar(10),
	nombre varchar(50),
	geometria public.geometry(point, 4326),
	CONSTRAINT enforce_dims_the_geom CHECK ((st_ndims(geometria) = 2)),
	CONSTRAINT enforce_geotype_the_geom CHECK (((geometrytype(geometria) = 'POINT'::text) OR (geometria IS NULL))),
	CONSTRAINT enforce_srid_the_geom CHECK ((st_srid(geometria) = 4326)),
	CONSTRAINT geometry_valid_check CHECK (st_isvalid(geometria)),
	CONSTRAINT odf_codigo unique (codigo)
);


insert into foodf (codigo, nombre) values ('ODF-HIPO', 'Hipodromo');
insert into foodf (codigo, nombre) values ('ODF-TECN', 'Edif. Tecnico');


create table FODIO (
	id serial primary key,
	codigo smallint,
	descripcion varchar(100),
	sala smallint,
	rack smallint,
	tipo varchar(20),
	subtipo varchar(20),
	odf integer,
	tabla varchar(30),
	externo integer,
	constraint fo_dio_odf foreign key (odf) references foodf (id)
);


create table FOCABLE (
	id serial primary key,
	codigo varchar(30),
	tipo varchar(20),
	subtipo varchar(20),
	capacidad smallint,
	buffer smallint,
	marca varchar(20),
	geometria public.geometry(point, 4326),
	CONSTRAINT enforce_dims_the_geom CHECK ((st_ndims(geometria) = 2)),
	CONSTRAINT enforce_geotype_the_geom CHECK (((geometrytype(geometria) = 'LINE'::text) OR (geometria IS NULL))),
	CONSTRAINT enforce_srid_the_geom CHECK ((st_srid(geometria) = 4326)),
	CONSTRAINT geometry_valid_check CHECK (st_isvalid(geometria)),
	CONSTRAINT fo_cable_codigo unique (codigo)
);

insert into focable (codigo, tipo, capacidad, buffer) values ('TRN1', 'TRONCAL', 24, 8);

-- FIBRA

create table FOHILO (
	id serial primary key,
	hilo smallint,
	posicion smallint,
	color varchar(10),
	buffer smallint,
	colorbuffer varchar(10),
	ststecnico varchar(10),
	stsocupacion varchar(10),
	stsoperativo varchar(10),
	cable integer,
	constraint fo_hilo_cable foreign key (cable) references focable (id)
);


create table FOENLACE (
	id serial primary key,
	codigo varchar(10),
	descripcion varchar(100),
	tipo varchar(20),
	subtipo varchar(20),
	capacidad smallint
);

insert into foenlace (codigo, descripcion, tipo, capacidad) values ('SAL1', 'Troncal a XXX', 'TRONCAL', 24);


create table FOENLACEDET (
	id serial primary key,
	idenlace integer,
	posicion smallint,
	idhilo integer,
	fila smallint,
	columna smallint,
	constraint fo_enlace_det foreign key (idenlace) references foenlace (id),
	constraint fo_enlace_hilo foreign key (idhilo) references fohilo (id)
);


create table FOCONEXION (
	id serial primary key,
	codigo varchar(10),
	descripcion varchar(100),
	tipo varchar(20),
	subtipo varchar(20)
);


