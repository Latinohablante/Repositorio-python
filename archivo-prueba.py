import time

v = time.timezone()
#asctime() = Tue Oct 24 15:57:22 2023
#localtime() = time.struct_time(tm_year=2023, tm_mon=10, tm_mday=24, tm_hour=15, tm_min=58, tm_sec=53, tm_wday=1, tm_yday=297, tm_isdst=0)

print(v)

empleado = {"Nombre": "Sergio Medina", "cargo":"programador", "salario":4000000}

print(list(empleado.keys())[0])