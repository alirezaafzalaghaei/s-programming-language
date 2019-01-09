[A1] IF X1 != 0 GOTO B1
Z1 <- Z1 + 1
IF Z1 != 0 GOTO C1
[B1] X1 <- X1 - 1
Y <- Y + 1
Z1 <- Z1 + 1
IF Z1 != 0 GOTO A1

[C1] IF X2 != 0 GOTO D1
Z2 <- Z2 + 1
IF Z2 != 0 GOTO A2
[D1] X2 <- X2 - 1
Z3 <- Z3 + 1
Z2 <- Z2 + 1
IF Z2 != 0 GOTO C1

[A2] IF Z3 != 0 GOTO B2
Z4 <- Z4 + 1
IF Z4 != 0 GOTO E1
[B2] Z3 <- Z3 - 1
Y <- Y + 1
Z5 <- Z5 + 1
IF Z5 != 0 GOTO A2