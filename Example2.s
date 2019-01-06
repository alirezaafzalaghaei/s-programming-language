[A] IF X1 != 0 GOTO B
Z1 <- Z1 + 1
IF Z1 != 0 GOTO C
[B] X1 <- X1 - 1
Y <- Y + 1
Z1 <- Z1 + 1
IF Z1 != 0 GOTO A

[C] IF X2 != 0 GOTO D
Z2 <- Z2 + 1
IF Z2 != 0 GOTO A2
[D] X2 <- X2 - 1
Z3 <- Z3 + 1
Z2 <- Z2 + 1
IF Z2 != 0 GOTO C

[A2] IF Z3 != 0 GOTO B2
Z4 <- Z4 + 1
IF Z4 != 0 GOTO E
[B2] Z3 <- Z3 - 1
Y <- Y + 1
Z5 <- Z5 + 1
IF Z5 != 0 GOTO A2