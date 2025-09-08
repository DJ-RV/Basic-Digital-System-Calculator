# Basic-Digital-System-Calculator



# getDecimalPart()
usé esta funcion para obtener las partes decimales de las conversiones a decimal
tambien lo use para la parte decimal de decimal a binario pero como los de decimal a octal
y decimal a hexadecimal los hice en la función respectiva porque me dió flojera ponerlo en la otra

# toBinary()
convierte de cualquier base a binario.

# toOctal()
convierte de cualquier base a octal.

# toDecimal()
convierte de cualquier base a decimal. La mayoría de lo importante está acá porque reutilizo la función.

# toHexadecimal()
convierte de cualquier base a binario. 

# el resto son funciones que corren junto al customtkinter

# showOut()
actualiza el label en el que se muestran los resultados.

# run()
a la orden del boton de conversion, utilizando la entrada y salida especificada por
el usuario, realiza la conversion.

# DETALLES IMPORTANTES
en distintas operaciones, sobretodo en el cambio de bases, redondee los valores a 5 decimales, ya que 
en ciertas operaciones, aunque el resultado obetenido era correcto, los procesos requeridos
para llegar al resultado eran ridiculamente largos.
un ejemplo particularmente terrible de esto era de octal a binario.

otro detalle es que por los mismos criterios vistos en clases, si los decimales son menores que 0.1 el código no los considera. Esto se puede cambiar y solo es para agilizar la calculadora. Por esta razón algunas transformaciones (ej= 123.123base16 a binario) entregan un número sin decimales.