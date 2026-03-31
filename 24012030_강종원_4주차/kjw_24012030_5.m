f1 = @(x) 30*x.^2-300*x+4;
fplot(f1,[-10 10])
fminbnd(f1, 4, 6)