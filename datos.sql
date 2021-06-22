CREATE TABLE cliente (

  dni       VARCHAR2(10) NOT NULL,

  pnombre     VARCHAR2(50) NOT NULL,

  snombre     VARCHAR2(50),

  appaterno    VARCHAR2(50) NOT NULL,

  apmaterno    VARCHAR2(50) NOT NULL,

  direccion    VARCHAR2(100) NOT NULL,

  fechanacimiento DATE NOT NULL

);



ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( dni );



CREATE TABLE detalle_venta (

  venta_nroventa  NUMBER(10) NOT NULL,

  producto_codigo NUMBER(10) NOT NULL

);



ALTER TABLE detalle_venta ADD CONSTRAINT pk_detalle_venta PRIMARY KEY ( venta_nroventa,

                                    producto_codigo );



CREATE TABLE producto (

  codigo     NUMBER(10) NOT NULL,

  nombre     VARCHAR2(30) NOT NULL,

  precio     NUMBER(7) NOT NULL,

  proveedor_rut VARCHAR2(10) NOT NULL

);



ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( codigo );



CREATE TABLE proveedor (

  rut    VARCHAR2(10) NOT NULL,

  nombre   VARCHAR2(50) NOT NULL,

  direccion VARCHAR2(100) NOT NULL

);



ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( rut );



CREATE TABLE venta (

  nroventa   NUMBER(10) NOT NULL,

  fechaventa  DATE NOT NULL,

  total    NUMBER(10) NOT NULL,

  cliente_dni VARCHAR2(10) NOT NULL

);



ALTER TABLE venta ADD CONSTRAINT venta_pk PRIMARY KEY ( nroventa );



ALTER TABLE detalle_venta

  ADD CONSTRAINT fk_producto FOREIGN KEY ( producto_codigo )

    REFERENCES producto ( codigo );



ALTER TABLE detalle_venta

  ADD CONSTRAINT fk_venta FOREIGN KEY ( venta_nroventa )

    REFERENCES venta ( nroventa );



ALTER TABLE producto

  ADD CONSTRAINT producto_proveedor_fk FOREIGN KEY ( proveedor_rut )

    REFERENCES proveedor ( rut );



ALTER TABLE venta

  ADD CONSTRAINT venta_cliente_fk FOREIGN KEY ( cliente_dni )

    REFERENCES cliente ( dni );



--INSERTAR DATOS EN LAS TABLAS

--DATOS TABLA CLIENTE

INSERT INTO CLIENTE VALUES ('111-2', 'MAXIMILIANO', 'PATRICIO', 'CONTRERAS', 'NILO', 'SU CASA 123', 

TO_DATE('27/12/2000','DD/MM/YYYY'));

INSERT INTO CLIENTE VALUES ('222-3', 'ALVARO', NULL, 'NUÑEZ', 'FERNANDEZ', 'AVDA SIEMPRE VIVA 456', 

TO_DATE('12/08/1977','DD/MM/YYYY'));



SELECT * FROM CLIENTE;

--DATOS TABLA PROVEEDOR



--DATOS TABLA PRODUCTO



--DATOS TABLA VENTA



--DATOS TABLA DETALLE