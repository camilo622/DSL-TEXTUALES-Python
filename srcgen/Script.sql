CREATE DATABASE script;

CREATE TABLE Persona (
	cedula int,
	nombre varchar (255),
	apellido varchar (255),
	direccion varchar (255),
	edad int,
	telefono varchar (255),
    correo varchar (255)
   );

  

CREATE TABLE Trabajo (
	id int,
	direccion varchar (255),
	ciudad varchar (255),
    pais varchar (255)
   );

  

CREATE TABLE Telefono (
	id int,
	indicador varchar (255),
    numero varchar (255)
   );

   
   ALTER TABLE Persona
ADD CONSTRAINT FK_Cedula
FOREIGN KEY (CedulaID) REFERENCES Persona(Cedula); 
 
   ALTER TABLE Trabajo
ADD CONSTRAINT FK_Id
FOREIGN KEY (IdID) REFERENCES Persona(Id); 
 
   ALTER TABLE Telefono
ADD CONSTRAINT FK_Id
FOREIGN KEY (IdID) REFERENCES Persona(Id); 
