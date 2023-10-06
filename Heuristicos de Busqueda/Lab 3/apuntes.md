
current <-- best(vecindad)

sigma <-- (i-1)

if Mejora(current, sigma):

    Actualizar sigma

else:

| .                                                                                                        <br /><br /><br /><br /><br /><br /><br /><br /><br /> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Simulated Anneling:

    Una simulacion parecida al destemple en un mapa de calor. e⁻DeltaE/T donde DeltaE es el cambio en el fitness y la temperatura son las iteraciones del programa

    Genera un punto de corte probabilistico [.............|Pn|............], luego se decide si el candidato peor se coge o no, mediante un np.random() < Pn

    Temperatura: 1 / step, por ejemplo

* Tabu Search:

    Se guardan los candidatos peores en un buffer

* Demonio:

    Se simula una cantidad de Energia que el "demonio" va a gastar para poder coger un candidato peor


| T \ AE | 1            | 10      | 50    | 100    | 150    | 250    | 500    |
| ------ | ------------ | ------- | ----- | ------ | ------ | ------ | ------ |
| 1      | 1/e          | 0.00004 | 1/50e | 1/100e | 1/150e | 1/250e | 1/500e |
| 10     | e⁰'¹       | 1/e     |       |        |        |        |        |
| 50     | e⁰'⁰⁵     |         | 1/e   |        |        |        |        |
| 100    | e⁰'⁰¹     |         |       | 1/e    |        |        |        |
| 150    | e⁰'¹       |         |       |        | 1/e    |        |        |
| 250    | e⁰'⁰⁰⁴   |         |       |        |        | 1/e    |        |
| 500    | e⁰'⁰⁰⁰² |         |       |        |        |        | 1/e    |
