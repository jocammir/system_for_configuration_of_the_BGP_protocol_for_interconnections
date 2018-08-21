import graficos as gf
import conexion_mysql as sql

conn=sql.realizar_conexion()
if conn==-1:
    gf.error_servidor()
else:
    gf.inicio(conn)
    sql.cerrar_conexion(conn)
