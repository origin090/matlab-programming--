f = @(x) 0.3*x - sin(2*x);

fplot(f, [0 4])
grid on

root = fzero(f,[0 4])

x_min = fminbnd(f, 0, 4)
y_min = f(x_min)

fplot(@(x) 0.3-2*cos(2*x), [0 4])
grid on
f(fzero(@(x) 0.3-2*cos(2*x),0.5)) %fzero(@(x) 0.3-2*cos(2*x),0.5)=x_min
f(fzero(@(x) 0.3-2*cos(2*x),2.5))
f(fzero(@(x) 0.3-2*cos(2*x),3.5))
