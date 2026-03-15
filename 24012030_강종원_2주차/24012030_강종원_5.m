x=0:0.01:2 ;
u=3*log10(70*x+1) ;
plot(x,u)
hold on

x=0:0.01:2 ;
v=4*cos(7*x) ;
plot(x,v)
xlabel('mile')
ylabel('mile/time')
grid on