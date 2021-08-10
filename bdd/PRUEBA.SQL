CREATE TABLE beneficiarios (
    numerofolio                     NUMBER(2) NOT NULL,
    fecha                           DATE NOT NULL,
    nombre                          VARCHAR2(20) NOT NULL,
    sexo                            CHAR(1) NOT NULL,
    direccion                       VARCHAR2(50) NOT NULL,
    comuna                          VARCHAR2(30) NOT NULL,
    ciudad                          VARCHAR2(30) NOT NULL,
    region                          VARCHAR2(30) NOT NULL,
    fonoparticular                  NUMBER(7),
    celular                         NUMBER(9) NOT NULL,
    email                           VARCHAR2(320),
    fechanacimiento                 DATE NOT NULL,
    estatura                        NUMBER(3) NOT NULL,
    peso                            NUMBER(3) NOT NULL,
    gruposanguineo                  VARCHAR2(4) NOT NULL,
    comunas_idcomunas               NUMBER(5) NOT NULL,
    regiones_idregion               NUMBER(3) NOT NULL,
    convenio_convenio_id            NUMBER NOT NULL,
    prevision_prevision_id          NUMBER NOT NULL,
    seguro_medico_seguro_medico_id  NUMBER NOT NULL
   
);


COMMENT ON COLUMN beneficiarios.sexo IS
    'f
m';

ALTER TABLE beneficiarios ADD CONSTRAINT beneficiarios_pk PRIMARY KEY ( numerofolio );

CREATE TABLE comunas (
    idcomunas  NUMBER(5) NOT NULL,
    nombre     VARCHAR2(30) NOT NULL
);

ALTER TABLE comunas ADD CONSTRAINT comunas_pk PRIMARY KEY ( idcomunas );

CREATE TABLE convenio (
    convenio              CHAR(1) NOT NULL,
    nombrecentroatencion  VARCHAR2(30) NOT NULL,
    direccion             VARCHAR2(50) NOT NULL,
    telefono              NUMBER(9) NOT NULL,
    medicos_idmedico      NUMBER(5) NOT NULL,
    convenio_id           NUMBER NOT NULL
);

COMMENT ON COLUMN convenio.convenio IS
    'si
no';

ALTER TABLE convenio ADD CONSTRAINT convenio_pk PRIMARY KEY ( convenio_id );

CREATE TABLE cto_emerg (
    nombre                     VARCHAR2(15) NOT NULL,
    relacion                   VARCHAR2(15) NOT NULL,
    fonoparticular             NUMBER(7),
    fonotrabajo                NUMBER(7) NOT NULL,
    celular                    NUMBER(9) NOT NULL,
    beneficiarios_numerofolio  NUMBER(2) NOT NULL
);

CREATE TABLE medicos (
    nombre    VARCHAR2(20) NOT NULL,
    idmedico  NUMBER(5) NOT NULL,
    telefono  NUMBER(7) NOT NULL
    
);

ALTER TABLE medicos ADD CONSTRAINT medicos_pk PRIMARY KEY ( idmedico );

CREATE TABLE prevision (
    tipoprevencion  CHAR(1) NOT NULL,
    prevision_id    NUMBER NOT NULL
);

COMMENT ON COLUMN prevision.tipoprevencion IS
    'FONASA
ISAPRE
OTRO';

ALTER TABLE prevision ADD CONSTRAINT prevision_pk PRIMARY KEY ( prevision_id );

CREATE TABLE regiones (
    idregion  NUMBER(3) NOT NULL,
    nombre    VARCHAR2(30) NOT NULL
);

ALTER TABLE regiones ADD CONSTRAINT regiones_pk PRIMARY KEY ( idregion );

CREATE TABLE seguro_medico (
    compañia          VARCHAR2(20) NOT NULL,
    numpoliza         NUMBER(30) NOT NULL,
    fono              NUMBER(7),
    seguro            CHAR(1) NOT NULL,
    seguro_medico_id  NUMBER NOT NULL
);

COMMENT ON COLUMN seguro_medico.seguro IS
    'si
no';

ALTER TABLE seguro_medico ADD CONSTRAINT seguro_medico_pk PRIMARY KEY ( seguro_medico_id );

ALTER TABLE beneficiarios
    ADD CONSTRAINT beneficiarios_comunas_fk FOREIGN KEY ( comunas_idcomunas )
        REFERENCES comunas ( idcomunas );

ALTER TABLE beneficiarios
    ADD CONSTRAINT beneficiarios_convenio_fk FOREIGN KEY ( convenio_convenio_id )
        REFERENCES convenio ( convenio_id );

ALTER TABLE beneficiarios
    ADD CONSTRAINT beneficiarios_prevision_fk FOREIGN KEY ( prevision_prevision_id )
        REFERENCES prevision ( prevision_id );

ALTER TABLE beneficiarios
    ADD CONSTRAINT beneficiarios_regiones_fk FOREIGN KEY ( regiones_idregion )
        REFERENCES regiones ( idregion );

ALTER TABLE beneficiarios
    ADD CONSTRAINT beneficiarios_seguro_medico_fk FOREIGN KEY ( seguro_medico_seguro_medico_id )
        REFERENCES seguro_medico ( seguro_medico_id );

ALTER TABLE convenio
    ADD CONSTRAINT convenio_medicos_fk FOREIGN KEY ( medicos_idmedico )
        REFERENCES medicos ( idmedico );

ALTER TABLE cto_emerg
    ADD CONSTRAINT cto_emerg_beneficiarios_fk FOREIGN KEY ( beneficiarios_numerofolio )
        REFERENCES beneficiarios ( numerofolio );

CREATE SEQUENCE convenio_convenio_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER convenio_convenio_id_trg BEFORE
    INSERT ON convenio
    FOR EACH ROW
    WHEN ( new.convenio_id IS NULL )
BEGIN
    :new.convenio_id := convenio_convenio_id_seq.nextval;
END;
/

CREATE SEQUENCE prevision_prevision_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER prevision_prevision_id_trg BEFORE
    INSERT ON prevision
    FOR EACH ROW
    WHEN ( new.prevision_id IS NULL )
BEGIN
    :new.prevision_id := prevision_prevision_id_seq.nextval;
END;
/

CREATE SEQUENCE seguro_medico_seguro_medico_id START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER seguro_medico_seguro_medico_id BEFORE
    INSERT ON seguro_medico
    FOR EACH ROW
    WHEN ( new.seguro_medico_id IS NULL )
BEGIN
    :new.seguro_medico_id := seguro_medico_seguro_medico_id.nextval;
END;

CREATE SEQUENCE SEQ_NUMEROFOLIO;

INSERT INTO beneficiarios VALUE (SEQ_NUMEROFOLIO.nextval, to_date('04-04-2016', 'DD/MM/YYYY'), 'DHARMA', 'f', "MI CASA", "LA FLORIDA", "SANTIAGO", 'METROPOLITANA', 1234567, "ASD@GMAIL.COM", to_date('03-05-2017', 'DD/MM/YYYY'), 169, 80, "OA")
INSERT INTO beneficiarios VALUE (SEQ_NUMEROFOLIO.nextval, to_date('04-04-2016', 'DD/MM/YYYY'), 'DHARMA', 'f', "MI CASA", "LA FLORIDA", "SANTIAGO", 'METROPOLITANA', 1234567, "ASD@GMAIL.COM", to_date('03-05-2017', 'DD/MM/YYYY'), 169, 80, "OA")
INSERT INTO beneficiarios VALUE (SEQ_NUMEROFOLIO.nextval, to_date('04-04-2016', 'DD/MM/YYYY'), 'DHARMA', 'f', "MI CASA", "LA FLORIDA", "SANTIAGO", 'METROPOLITANA', 1234567, "ASD@GMAIL.COM", to_date('03-05-2017', 'DD/MM/YYYY'), 169, 80, "OA")
INSERT INTO beneficiarios VALUE (SEQ_NUMEROFOLIO.nextval, to_date('04-04-2016', 'DD/MM/YYYY'), 'DHARMA', 'f', "MI CASA", "LA FLORIDA", "SANTIAGO", 'METROPOLITANA', 1234567, "ASD@GMAIL.COM", to_date('03-05-2017', 'DD/MM/YYYY'), 169, 80, "OA")
