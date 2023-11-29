import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuario
db = orm.SQLiteORM('db_biblioteca')
#creamos las tablas
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuario)

autor_uno = {
    "DNI":66376,
    "Nombre":"quevedo",
    "Apellidos":"escoja de los rios"}

Usuarios = [
    {
        "DNI":347843,
        "Nombre":"feli",
        "Apellido":"ccachahua",
        "F_nacimiento":"12/12/1923",
        "Estado":"Activo"
    },
    {
        "DNI":8348438,
        "Nombre":"Orlando",
        "Apellido":"de type",
        "F_nacimiento":"12/12/1923",
        "Estado":"Inactivo"
    },
    {
        "DNI":347443,
        "Nombre":"chamo1",
        "Apellido":"no jodas",
        "F_nacimiento":"30/12/2023",
        "Estado":"Activo"
    },
    {
        "DNI":347243,
        "Nombre":"yadira",
        "Apellido":"medina",
        "F_nacimiento":"12/12/1923",
        "Estado":"Activos"
    }
]
#insertamos datos
#db.insertarUno("Autores",autor_uno)
#db.insertarVarios('Usuarios',Usuarios)

#print(db.mostrar(Usuarios))
#print(db.mostrar("Usuarios",where="Nombre LIKE '%mo'", type="objeto"))
#print(db.mostrar("Usuarios"))
# db.actualizar("Usuarios",{"estado":"desactivado"},where="Nombre = 'yadira'")
# db.actualizar("Usuarios",{"F_nacimiento":"30/12/2023"}, where="F_nacimiento = '!=12'")
db.eliminar("Usuarios",where="Nombre='Orlando'")
print(db.mostrar("Usuarios", type="objeto"))