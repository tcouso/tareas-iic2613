% PRE PROCESAMIENTO DEL MAPA

% el grafo del mapa es no dirigido y cada nodo conecta consigo mismo
camino(L1,L2) :- camino(L2,L1).
camino(L,L) :- lugar(L).


% ENCONTRAR EL CULPABLE

% definicion de alcanzable
alcanzable(L1,L2,T1,T2) :- camino(L1,L2), tiempo(T1), tiempo(T2), T2>T1.
alcanzable(L1,L3,T1,T3) :- alcanzable(L1,L2,T1,T2), alcanzable(L2,L3,T2,T3).

% casos de mentira

% afirmar que alguien estaba en un lugar diferente del que estaba
mentira1(P) :- personaEnLugar(Q,L1,T), afirmacionLugar(P,Q,L2,T), L1!=L2.

% afirmar que alguien estaba en dos lugares al mismo tiempo
mentira2(P) :- afirmacionLugar(P,Q,L1,T), afirmacionLugar(P,Q,L2,T), L1!=L2.

% afirmar que alguien fue de un lugar a otro en un tiempo insuficiente
mentira3(P) :- afirmacionLugar(P,Q,L1,T1), afirmacionLugar(P,Q,L2,T2), not alcanzable(L1,L2,T1,T2), L1!=L2.

% afirmar que alguien fue a un lugar desde otro lugar donde se sabe que estuvo en un tiempo insuficiente
mentira4(P) :- afirmacionLugar(P,Q,L1,T1), personaEnLugar(Q,L2,T2), not alcanzable(L1,L2,T1,T2), L1!=L2.

% afirmar algo que al menos dos personas contradicen de manera coordinada, en tanto solo una persona puede mentir
mentira5(P1) :- afirmacionLugar(P1,Q,L1,T), afirmacionLugar(P2,Q,L2,T), afirmacionLugar(P3,Q,L2,T), L1!=L2, P1!=P2, P1!=P3, P2!=P3.
mentira6(P1) :- afirmacionLugar(P1,Q1,L,T), afirmacionLugar(P2,Q2,L,T), afirmacionLugar(P3,Q2,L,T), Q1!=Q2, P1!=P2, P1!=P3, P2!=P3.

% presunto inocente
presuntoInocente(P) :- persona(P), not culpable(P).

% relato de presunto inocente se asume verdadero
personaEnLugar(Q,L,T) :- afirmacionLugar(P,Q,L,T), presuntoInocente(P).

% sospechoso
sospechoso(P) :- persona(P), lugar(L), descubrimiento(L,T2), tiempo(T2), #count{T1: personaEnLugar(P,L,T1), T1<T2} >= 3.

% culpable
culpable(P) :- 1 {mentira1(P); mentira2(P); mentira3(P); mentira4(P); mentira5(P); mentira6(P)} 6, persona(P).

% hay un unico culpable
1 {persona(P): culpable(P)} 1.


% VERSIÓN VÁLIDA DE LOS HECHOS

% El supuesto usado en esta implementación es que en un relato válido, las personas se encuentran inicialmente
% en lugares aleatorios, desde los cuales pueden moverse o esperar en cada tiempo. La validez del relato 
% depende de que sea consistente con los hechos; esto implica que los lugares que visitan las personas en 
% el relato son consistentes con los lugares en los que efectivamente se encontraban.


action(moverse).
% action(esperar).

% ubicación inicial de las personas
1 {relatoPersonaEnLugar(P,L,T): lugar(L)} 1 :- persona(P), tiempo(T), T=1.

% acciones de las personas
1 {relatoPersonaEnLugar(P,L2,T+1): camino(L1,L2)} 1 :- relatoPersonaEnLugar(P,L1,T), exec(P,moverse,T).
% relatoPersonaEnLugar(P,L,T+1) :- relatoPersonaEnLugar(P,L,T), exec(P,esperar,T).

% las personas ejecutaran una acción en cada momento
% 1{exec(P,moverse,T); exec(P,esperar,T)}1 :- persona(P), tiempo(T+1).
exec(P,moverse,T) :- persona(P), tiempo(T+1).


% dos personas no pueden estar en el mismo lugar al mismo tiempo
:- relatoPersonaEnLugar(P1,L,T), relatoPersonaEnLugar(P2,L,T), P1!=P2. 

% el culpable debe visitar el lugar del crimen antes del descubrimiento
:-  culpable(P), descubrimiento(L,T2), #count{T1: relatoPersonaEnLugar(P,L,T1), T1<T2} = 0.

% la presencia de una persona en el relato debe coincidir con su presencia en la realidad
:- relatoPersonaEnLugar(P,L1,T), personaEnLugar(P,L2,T), L1!=L2.
:- relatoPersonaEnLugar(P1,L,T), personaEnLugar(P2,L,T), P1!=P2.

% un presunto inocente es sospechoso si en el relato visito el lugar de descubrimiento en a lo menos tres ocasiones
sospechoso(P) :- persona(P), lugar(L), descubrimiento(L,T2), tiempo(T2), #count{T1: relatoPersonaEnLugar(P,L,T1), T1<T2} >= 3.

% Queremos el relato donde el número de sospechosos sea mínimo
#minimize{1,P: sospechoso(P)}.


#show culpable/1.
#show sospechoso/1.
#show relatoPersonaEnLugar/3.
