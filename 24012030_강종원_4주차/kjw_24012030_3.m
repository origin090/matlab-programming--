%사용자 정의 함수, 파일명 cone_area로 저장
function A = cone_area(r)
global V
A = sqrt(pi^2*r^6+9*V^2)/r;
end

%command 창
global V
V = 10;
r_min = fminbnd(@cone_area, 0.1, 10)
A_min = cone_area(r_min)
h = 3*V/(pi*r_min^2)
fplot(@cone_area, [0.1 10])
grid on
A_inc = 1.1*A_min;
f = @(r) cone_area(r) - A_inc;
r1 = fzero(f, r_min - 0.5)
r2 = fzero(f, r_min + 0.5)
% 면적이 최솟값 위로 10% 증가하기 전 r1 ≤ r ≤ r2 범위에 있음