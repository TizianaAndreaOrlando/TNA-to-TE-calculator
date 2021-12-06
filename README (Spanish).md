# Calculadora de TNA a TE

Para el lector:

El programa nos permite calcular dada una TNA (tasa nominal anual) una TE (tasa efectiva). 
A modo de introducción: La TNA es una tasa de interés ofrecida por instituciones bancarias en las que se especifica un periodo de tiempo 'x' donde se realizaran los pagos. Por otro lado, la TE es la cantidad de interés que obtendremos efectivamente de la operación realizada en el periodo x deseado. Tenemos también lo que es la TEA (tasa efectiva anual) donde se refleja lo que efectivamente ganaremos en conceptos de interés en el periodo de un año.  

## ¿Donde puedo encontrar la TNA?
A la hora de hacer operaciones financieras con instituciones bancarias. Por ejemplo, si nosotros como inversores queremos realizar una operación de plazo fijo vamos a tener un prospecto (elaborado por el banco de elección) donde se reflejaran tanto la TNA la TEA entre otras cosas y los distintos porcentajes. 

## Caso hipotético

Supongamos que tenemos una TNA(x) = 24%. Donde x representa el perido de tiempo (supongamos x = 30 días). Al finalizar el año, nosotros obtendremos una rentabilidad del 24% por cada unidad monetaria invertida y por haber invertido cada 30 días en un lapso de tiempo de un año (por esto es anual). La principal diferencia entre una TNA y una TE es que la TNA se basa en una operacion de interes simple y no compuesta donde no hay reinversión de los intereses en cada periodo. Ahora si queremos hablar de una TE asumimos que la cantidad ganada por periodo es reinvertida por lo que el resultado entre una TNA y una TE serán diferentes... La TEA (tasa efectiva anual) siempre será mayor que la TNA. Las tasas efectivas estan ligadas al concepto de interes compuesto en vez de interes simple como ya habia mencionado. 

## ¿Como funciona el pasaje entre tasas efectivas?

Una vez que tenemos la TE(x) (la tasa efectiva en un periodo especifico), si cambiamos el periodo vamos a tener, por supuesto, una tasa diferente en nuestra operación. No es lo mismo una TE(30) que una TE(90) y la lógica de esto, además de una cuestión meramente matemática, proviene de que en el caso del TE(30) la institución bancaria retiene nuestro dinero por un periodo de tiempo menor al de la TE(90) por lo que también es razonable pensar que la TE(90) nos brindará un interés mayor al tener nuestro dinero un tiempo mayor inmovilizado en la operación teniendo nosotros como inversores menor liquidez durante ese periodo de tiempo. 

## ¿Por qué implementé este software?

Principalmente porque mi objetivo inicial era hacer las cosas más sencillas en el día a día, es decir; Si no tengo los recursos necesarios a mano y solamente estoy usando la computadora, me parecía mucho más practico usar el software en vez de realizar los cálculos a mano/ con calculadora que no tiene programada las formulas y en ese caso, podría cometer el error de realizar mal los cálculos. Por otro lado, es un software que sirve para personas que no están inmersas en el ámbito financiero pero que aún así realizan este tipo de operaciones de inversión y quieren realizar los cálculos.
Como objetivo paralelo quería mejorar mis habilidades en la programación (en este caso utilizando Python) para poder crecer en el ambito y poder practicar. 

## Observaciones respecto del programa
* El programa está en Español.

* Trate de prevenir distintos tipos de errores por parte de los usuarios como lo son el error de tipeo pero problemas donde se debe de colocar un tipo de dato determinado (números por ejemplo) y se coloca otro tipo de dato distinto, provocará que el programa se cierre y se tenga que volver a ejecutar el mismo.

* Hay veces que el programa menciona una tasa distinta a la TNA y es la TNAA. La misma tiene la misma función que la TNA pero en este caso se esta haciendo una operación de descuento y no de capitalización. 

* El programa está establecido en 365 días por año. Hay muchas formas de tomar el tiempo para calcular la tasa pero trate de hacerlo simple. 

# Disfruten del programa!
Saludos, 

_Orlando Tiziana Andrea
