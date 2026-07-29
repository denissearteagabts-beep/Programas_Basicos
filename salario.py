salario_bruto=float(input("Ingrese el salario bruto"))
porcentaje=float(input("Ingrese el porcentaje de impuestos"))
deducciones=float(input("Ingrese las deducciones"))

impuestos=salario_bruto*(porcentaje/100)
salario_neto=salario_bruto-impuestos-deducciones

print("Tu salario neto es¨", salario_neto)