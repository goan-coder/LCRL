update_MDP(_,Y):-
    random_between(0, 499, Y).
trans(0,X/q0,Y/q1):-
    (X//20) mod 5 is 4,
    \+ ((X//20 ) mod 5)=:=((X//100) mod 5),
    update_MDP(X,Y).
 
trans(1,X/q0,Y/q2):-
    (X//20) mod 5 is 4,
    ((X//20 ) mod 5)=:=((X//100) mod 5),
    update_MDP(X,Y).
 
trans(2,X/q0,Y/q3):-
    \+ (X//20) mod 5 is 4,
    ((X//20 ) mod 5)=:=((X//100) mod 5),
    update_MDP(X,Y).
 
trans(3,X/q1,Y/q1):-
    (X//20) mod 5 is 4,
    \+ ((X//20 ) mod 5)=:=((X//100) mod 5),
    update_MDP(X,Y).
 
trans(4,X/q1,Y/q2):-
    ((X//20 ) mod 5)=:=((X//100) mod 5),
    update_MDP(X,Y).
 
trans(5,X/q2,Y/q2):-
    print('reached q2'),
    update_MDP(X,Y).
 
trans(6,X/q3,Y/q3):-
    update_MDP(X,Y),
    (x//20) mod 5 is 4.
 
trans(7,X/q3,Y/q2):-
    update_MDP(X,Y),
    \+ (x//20) mod 5 is 4.
ts(X/S,X/S).
ts(X/S,Y/S0):-
    trans(T,X/S,Z/S1),
    write('\n'),
    print(' Chosen edge(T) is '),
    print(T),
    print(' current state(S1) is '),
    print(S1),
    ts(Z/S1,Y/S0),
    !.
