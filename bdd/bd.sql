CREATE TABLE formulario
(
    numeroCarnetSocio int(10) not null auto increment, 
    fechaSolicitud datetime not null,
	rut varchar(10) not null, 
	primerNombre varchar(15) not null, 
	segundoNombre varchar(15) not null,
    apellidoPaterno varchar(15) not null, 
    apellidoMaterno varchar(15) not null, 
    fechaNacimiento date not null,
    numeroPasaporte varchar(20), 
    pretencionDeSueldo int(8) not null, 
    direccion varchar(20) not null,
    region varchar(20) not null, 
    comuna varchar(20) not null, 
    genero varchar(10) not null, 
    discapacidad varchar(20),
    tipoDiscapacidad varchar(20), 
    nacionalidad varchar(15), 
    correoElectronico varchar(320) not null,
    telefono varchar(15) not null, 
    tipoNumeroTelefono varchar(15) not null, 
    IdCurriculumVitae int(10) not null,
    IdCarga int(10),constraint PK_FORMULARIO primary key (numeroCarnetSocio),
    constraint RUT_F unique (rut),
    constraint FK_FORMULARIO_CURRICULUM foreign key (IdCurriculumVitae)
    references curriculumVitae(IdCurriculumVitae),
    constraint FK_FORMULARIO_CARGA foreign key (Idcarga) references carga(IdCarga)
);



CREATE TABLE curriculumVitae
(
    IdCurriculumVitae int(10) not null auto increment,
	fechaCreacion date not null, 
	constraint PK_CV primary key (IdCurriculumVitae)
);
                                
CREATE TABLE carga 
( 
    IdCarga int(10) not null auto increment,
    rutCarga varchar(10) not null, 
    nombreCarga varchar(20) not null, 
    segundoNombreCarga varchar(20) not null,
	apellidoPaternoCarga varchar(20) not null, 
	apellidoMaternoCarga varchar(20) not null, 
	fechaNacimientoCarga date not null,
    tipoDeParentesco varchar(20) not null, 
    constraint PK_CARGA primary key (IdCarga), 
    constraint RUT_C unique (rutCarga)
);
                        
CREATE TABLE beneficios 
( 
    idBeneficio int(10) not null auto increment, 
    numeroCarnetSocio int(10) not null, 
    tipoBeneficio varchar(20) not null, 
    cantidadDeUsos int(10) not null,
	constraint PK_BENEFICIOS primary key (idBeneficio), 
	constraint FK_FORMULARIO_BENEFICIO foreign key (numeroCarnetSocio) references formulario(numeroCarnetSocio)
);                        
                                
 CREATE TABLE vehiculo 
 (
    idVehiculo int(10) not null auto increment, 
    marcaVehiculo varchar(15), modelo varchar(15), 
    patenteVehiculo varchar(6), color varchar(15),
	tipoVehiculo varchar(15), 
	numeroDeChasis varchar(20), 
	numeroDeMotor varchar(20), 
	numeroCarnetSocio int(10), 
	constraint PK_VEHICULO primary key (idVehiculo),
    constraint FK_VEHICULO_FORMULARIO foreign key (numeroCarnetSocio) references formulario(numeroCarnetSocio)
);
                     
CREATE TABLE historialDePagos 
(
    idPago int(10) not null auto increment, 
    fechaPago date not null, 
    tipoDePago varchar(20) not null, 
    tipoBanco varchar(20), 
    numeroCheque varchar(20),
	numeroCarnetSocio int(10), 
	constraint PK_HISTORIALDEPAGOS primary key (idPago),
	constraint FK_HISTORIALDEPAGOS_FORMULARIO foreign key (numeroCarnetSocio) references formulario(numeroCarnetSocio)
); 