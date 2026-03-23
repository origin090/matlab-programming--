v0 = 50;
A = (5*pi)/18;
g = 9.81;
thit = (2*(v0)*sin(A))/g
ymax = ((v0)*sin(A))^2/(2*g)

t=[0:0.1:thit];
x = ((v0)*cos(A))*t ;
y = ((v0)*sin(A))*t-(g*(t.^2))/2 ;
plot(x,y)