#const bound = 14.
time(1..bound).

% define rangeZ
rangeZ(0..1).

% set of robot actions
action(up).
action(down).
action(left).
action(right).
action(wait).
action(lift).
% action(drop).

% robot executes one action at a time
1 {exec(R,A,T): action(A)} 1 :- robot(R),time(T+1).

% robot position
robotOn(R,X,Y+1,T+1) :- exec(R,up,T),robotOn(R,X,Y,T),robot(R),time(T+1).
robotOn(R,X,Y-1,T+1) :- exec(R,down,T),robotOn(R,X,Y,T),robot(R),time(T+1).
robotOn(R,X-1,Y,T+1) :- exec(R,left,T),robotOn(R,X,Y,T),robot(R),time(T+1).
robotOn(R,X+1,Y,T+1) :- exec(R,right,T),robotOn(R,X,Y,T),robot(R),time(T+1).
robotOn(R,X,Y,T+1) :- exec(R,wait,T),robotOn(R,X,Y,T),robot(R),time(T+1).
robotOn(R,X,Y,T+1) :- exec(R,lift,T),robotOn(R,X,Y,T),robot(R),time(T+1).

% box position
boxOn(B,X,Y,Z,T+1) :- boxOn(B,X,Y,Z,T), not exec(R,lift,T), not carryingBox(R,B,T), robot(R), box(B), rangeZ(Z), time(T+1), Z=0.
boxOn(B,X,Y,Z,T) :- carryingBox(R,B,T), robotOn(R,X,Y,T), robot(R), box(B), rangeZ(Z), Z=1.

% box is nearby robot
boxRight(B,R,T) :- robotOn(R,X,Y,T), boxOn(B,X+1,Y,0,T), robot(R), box(B).
boxLeft(B,R,T) :- robotOn(R,X,Y,T), boxOn(B,X-1,Y,0,T), robot(R), box(B).
boxUp(B,R,T) :- robotOn(R,X,Y,T), boxOn(B,X,Y+1,0,T), robot(R), box(B).
boxDown(B,R,T) :- robotOn(R,X,Y,T), boxOn(B,X,Y-1,0,T), robot(R), box(B).


% carrying box definition
carryingBox(R,B,T+1) :- exec(R,lift,T), 1 {boxUp(B,R,T); boxDown(B,R,T); boxRight(B,R,T); boxLeft(B,R,T)}, box(B), robot(R), time(T+1).
carryingBox(R,B,T+1) :- carryingBox(R,B,T), box(B), robot(R), time(T+1).
:- carryingBox(R,B,T), exec(R,lift,T), box(B), robot(R).

% range restrictions
:- robotOn(R,X,Y,T), not rangeX(X).
:- robotOn(R,X,Y,T), not rangeY(Y).

:- boxOn(B,X,Y,Z,T), not rangeX(X).
:- boxOn(B,X,Y,Z,T), not rangeY(Y).

% obstacle restrictions
:- robotOn(R,X,Y,T), obstacle(X,Y).
:- boxOn(B,X,Y,Z,T), obstacle(X,Y).

% collision restrictions
:- robotOn(R1,X,Y,T), robotOn(R2,X,Y,T), R1!=R2.
:- robotOn(R1,X,Y,T), robotOn(R2,X+1,Y,T), robotOn(R2,X,Y,T+1), robotOn(R1,X+1,Y,T+1).
:- robotOn(R1,X,Y,T), robotOn(R2,X,Y+1,T), robotOn(R2,X,Y,T+1), robotOn(R1,X,Y+1,T+1).

% there cannot be two boxes in the same place at the same time
:- boxOn(B1,X,Y,Z,T), boxOn(B2,X,Y,Z,T), B1!=B2.

% one box cannot be at two places at the same time
:- boxOn(B,X1,Y,Z,T), boxOn(B,X2,Y,Z,T), X1!=X2.
:- boxOn(B,X,Y,Z,T), robotOn(R,X,Y,T), not carryingBox(R,B,T), robot(R), box(B).

:- carryingBox(R1,B,T), carryingBox(R2,B,T), R1!=R2.
:- carryingBox(R,B1,T), carryingBox(R,B2,T), B1!=B2.

% goal definition
atGoal(B,T) :- boxOn(B,X,Y,Z,T), goal(X,Y), box(B).
:- box(B), not atGoal(B,bound).


% % model output filters
% #show robotOn/4.
% #show exec/3.
% #show carryingBox/3.
% #show boxOn/5.
% #show goal/2.


% we show the models that maximize the times the boxes spend at goal
#maximize{1,B,T: atGoal(B,T)}.
