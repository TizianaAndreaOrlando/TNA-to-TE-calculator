# Calculadora de TNA a TE

Para el lector:
El programa nos permite calcular dada una TNA (tasa nominal anual) una TE (tasa efectiva). A modo de introducción: La TNA, en finanzas, esta asociada a una tasa de interes ofrecida por instituciones bancarias en las que se especifica un periodo de tiempo 'x' donde los pagos se realizarán. Por otro lado, la TE es la cantidad de interes que obtendremos efectivamente de la operacion realizada en el periodo x deseado. 

## ¿Donde puedo encontrar la TNA?
Como mencioné recien, la misma es dada y utilizada por instituciones bancarias. Por ejepemplo, si nosostros como inversores queremos realizar una operación de plazo fijo. 

## Caso hipotetico

Supongamos que tenemos una TNA(x) = 24%. Donde x representa el perido de tiempo (supongamos x = 30 días), al finalizar el año, nosotros obtendremos una rentabilidad del 24% por cada unidad monetaria invertida y por haber invertido cada 30 días en un lapso de tiempo de un año (por esto es anual). La principal diferencia entre una TNA y una TE es que la TNA se basa en una operacion de interes simple y no compuesta donde no hay reinversión de los intereses en cada periodo. Ahora, si queremos hablar de una TE, asumimos que la cantidad ganada por periodo es reinvertida por lo que el resultado entre una TNA y una TE serán diferentes... La TEA (tasa efectiva anual) siempre será mayor que la TNA. Las tasas efectivas estan ligadas al concepto de interes compuesto en vez de interes simple como ya habia mencionado. 

## ¿Como funciona el pasaje entre tasas efectivas?

Una vez que tenemos la TE(x) (la tasa efectiva en un periodo especifico), si cambiamos el periodo vamos a tener, por supuesto, una tasa diferente en nuestra operacion. No es lo mismo una TE(30) que una TE(90) y la logica de esto, ademas de una cuestión meramente matematica, proviene de que en el caso del TE(30) la institución bancaria retiene nuestro dinero por un periodo de tiempo menor al de la TE(90) por lo que tambiene es razonable pensar que la TE(90) nos brindará un interes mayor al tener nuestro dinero un tiempo mayor inmobilizado en la operación teniendo nosotros como inversores menor liquidez durante ese periodo de tiempo. 

## ¿Por qué implemente este software?

Bueno, principalmente porque mi objetivo principal era hacer las cosas más sencillas en el día a día, es decir; Si no tengo lo recursos a mano y solamente estoy usando la computadora, me parecia mucho más practico usar el software que, en el caso de usar la calculadora, la misma no tiene programadas las formulas y podria cometer yo el error de realizar mal los calculos. Por otro lado, es un software que sirve para personas que no estan inmersas en el ambito financiero pero que aún así realizan actividades de bajo riesgo o conservadoras como lo son los palzos fijos.
Como objetivo paralelo, quería mejorar mis habilidades en la programación (en este caso utilizando Python) para poder crecer en el ambito y poder practicar. 

## Observaciones respecto del programa
* El programa esta en Español

* Trate de prevenir distintos tipos de errores por parte de los usuarios como lo son el error de tipeo pero problemas donde se debe de colocar un tipo de dato determinado (números por ejemplo) y se coloca otro tipo de dato distinto, provocará que el programa se cierre y se tenga que volver a ejecutar el mismo.

* Hay veces que el programa menciona una tasa distinta a la TNA y es la TNAA. La misma tiene la misma función que la TNA pero en este caso se esta haciendo una operación de descuento y no de capitalización. 

* El programa está establecido en 365 días por año. Hay muchas formas de tomar el tiempo para calcular la tasa pero trate de hacerlo simple. 

# Disfruten del programa!
Saludos, 

_Orlando Tiziana Andrea
