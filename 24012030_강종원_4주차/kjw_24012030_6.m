f = @(x) x.^2;
g = @(x) 3*cos(x);
h = @(x) 6*exp(x);
j = @(x) h(g(f(x)));
fplot(j,[0 4])