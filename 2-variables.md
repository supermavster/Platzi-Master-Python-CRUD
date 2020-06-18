# Variables and Expressions

Variables y expresiones
Una variable es simplemente el contenedor de un valor. Es una forma de decirle a la computadora de que nos guarde un valor para luego usarlo.

Python es un lenguaje dinámico, este concepto de privado y público se genera por convenciones del lenguaje. En programación el signo `=` significa asignación.

Si una variable esta en mayúscula, usualmente se refiere a una constante, no debería reasignarse. Es una convención.

# Reglas de Variables:

-   Pueden contener números y letras
-   No deben comenzar con número
-   Múltiples palabras se unen con \_
-   No se pueden utilizar palabras reservadas
-   Expresiones son instrucciones para el interprete para evaluar la expresión.
-   Los enunciados tienen efectos dentro del programa, como print que genera un output.

---

**Public:** `message = 'How are you?'`

**Private:** `_age = 22`

**Constants:** `PI = 3.14159`

**Super Private:** `__do_not_touch = 'RE-IMPORTANT'`

---

## Re-Assignation

```
my_var = 2
my_var *= 5
print(my_var) # 10
```

---

## Prioridad de operadores en funcionalidad

**PEMDAS** = Paréntesis, Exponente, Multiplicación-División, Adición-Sustracción

```
()                          #Parentesis
**                          #Exponentes
*, /, not                   #Multiplicación o División
+, -, and                   #Suma o Resta
>, <, ==, >=, <=, ! , or    #Operadores aritmeticos
```
