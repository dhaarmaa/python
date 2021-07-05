CREATE TABLE beneficios (
    idbeneficio        INTEGER NOT NULL,
    numerocarnetsocio  INTEGER NOT NULL,
    tipobeneficio      VARCHAR2(20) NOT NULL,
    cantidaddeusos     INTEGER NOT NULL
)
LOGGING;

ALTER TABLE beneficios ADD CONSTRAINT pk_beneficios PRIMARY KEY ( idbeneficio );

CREATE TABLE carga (
    idcarga               INTEGER NOT NULL,
    rutcarga              VARCHAR2(10) NOT NULL,
    nombrecarga           VARCHAR2(20) NOT NULL,
    segundonombrecarga    VARCHAR2(20) NOT NULL,
    apellidopaternocarga  VARCHAR2(20) NOT NULL,
    apellidomaternocarga  VARCHAR2(20) NOT NULL,
    fechanacimientocarga  DATE NOT NULL,
    tipodeparentesco      VARCHAR2(20) NOT NULL
)
LOGGING;

ALTER TABLE carga ADD CONSTRAINT pk_carga PRIMARY KEY ( idcarga );

ALTER TABLE carga ADD CONSTRAINT rut_c UNIQUE ( rutcarga );

CREATE TABLE curriculumvitae (
    idcurriculumvitae  INTEGER NOT NULL,
    fechacreacion      DATE NOT NULL
)
LOGGING;

ALTER TABLE curriculumvitae ADD CONSTRAINT pk_cv PRIMARY KEY ( idcurriculumvitae );

CREATE TABLE formulario (
    numerocarnetsocio   INTEGER NOT NULL,
    fechasolicitud      unknown 
--  ERROR: Datatype UNKNOWN is not allowed 
     NOT NULL,
    rut                 VARCHAR2(10) NOT NULL,
    primernombre        VARCHAR2(15) NOT NULL,
    segundonombre       VARCHAR2(15) NOT NULL,
    apellidopaterno     VARCHAR2(15) NOT NULL,
    apellidomaterno     VARCHAR2(15) NOT NULL,
    fechanacimiento     DATE NOT NULL,
    numeropasaporte     VARCHAR2(20),
    pretenciondesueldo  INTEGER NOT NULL,
    direccion           VARCHAR2(20) NOT NULL,
    region              VARCHAR2(20) NOT NULL,
    comuna              VARCHAR2(20) NOT NULL,
    genero              VARCHAR2(10) NOT NULL,
    discapacidad        VARCHAR2(20),
    tipodiscapacidad    VARCHAR2(20),
    nacionalidad        VARCHAR2(15),
    correoelectronico   VARCHAR2(320) NOT NULL,
    telefono            VARCHAR2(15) NOT NULL,
    tiponumerotelefono  VARCHAR2(15) NOT NULL,
    idcurriculumvitae   INTEGER NOT NULL,
    idcarga             INTEGER
)
LOGGING;

ALTER TABLE formulario ADD CONSTRAINT pk_formulario PRIMARY KEY ( numerocarnetsocio );

ALTER TABLE formulario ADD CONSTRAINT rut_f UNIQUE ( rut );

CREATE TABLE historialdepagos (
    idpago             INTEGER NOT NULL,
    fechapago          DATE NOT NULL,
    tipodepago         VARCHAR2(20) NOT NULL,
    tipobanco          VARCHAR2(20),
    numerocheque       VARCHAR2(20),
    numerocarnetsocio  INTEGER
)
LOGGING;

ALTER TABLE historialdepagos ADD CONSTRAINT pk_historialdepagos PRIMARY KEY ( idpago );

CREATE TABLE vehiculo (
    idvehiculo         INTEGER NOT NULL,
    marcavehiculo      VARCHAR2(15),
    modelo             VARCHAR2(15),
    patentevehiculo    VARCHAR2(6),
    color              VARCHAR2(15),
    tipovehiculo       VARCHAR2(15),
    numerodechasis     VARCHAR2(20),
    numerodemotor      VARCHAR2(20),
    numerocarnetsocio  INTEGER
)
LOGGING;

ALTER TABLE vehiculo ADD CONSTRAINT pk_vehiculo PRIMARY KEY ( idvehiculo );

ALTER TABLE beneficios
    ADD CONSTRAINT fk_formulario_beneficio FOREIGN KEY ( numerocarnetsocio )
        REFERENCES formulario ( numerocarnetsocio )
    NOT DEFERRABLE;

ALTER TABLE formulario
    ADD CONSTRAINT fk_formulario_carga FOREIGN KEY ( idcarga )
        REFERENCES carga ( idcarga )
    NOT DEFERRABLE;

ALTER TABLE formulario
    ADD CONSTRAINT fk_formulario_curriculum FOREIGN KEY ( idcurriculumvitae )
        REFERENCES curriculumvitae ( idcurriculumvitae )
    NOT DEFERRABLE;

ALTER TABLE historialdepagos
    ADD CONSTRAINT fk_historialdepagos_formulario FOREIGN KEY ( numerocarnetsocio )
        REFERENCES formulario ( numerocarnetsocio )
    NOT DEFERRABLE;

ALTER TABLE vehiculo
    ADD CONSTRAINT fk_vehiculo_formulario FOREIGN KEY ( numerocarnetsocio )
        REFERENCES formulario ( numerocarnetsocio )
    NOT DEFERRABLE;