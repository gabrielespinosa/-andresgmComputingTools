%Analisis Numerico
%Gabriel Espinosa y Mario Varon

clc;
clear;

k=input('ingrese el numero de terminos para realizar las sumas parciales k:\n');
n=input('ingrese el paso para realizar el vector x cuyo rango es de [-pi,pi] n:\n');

x=-pi:n:pi;
tam=size(x);%dimenciones de x

%Generacion de la funcion normal
for i=1:tam(2)
    if x(i)<0
        fn(i)=-1;
    else
        fn(i)=1;
    end
end

%generacion de la funcion a partir de Fourier
for i=1:tam(2)
    for j=1:k
        termino(k)=2/(k*pi)*(1-((-1)^k))*sin(k*x(i));%hallar cada termino
    end
    for h=1:k
        if h>1
            f(h)=termino(k)+f(h-1);%hallar f(x(i)) sumando los terminos ecuacion determinado por el modelo de fourier
        else
            f(i)=termino(k);
        end 
    end
end

%Graficas
plot(x,fn,'b')

grid on
axis square
axis ([-pi pi -1 1])
legend('funcion normal')
xlabel('x')
ylabel('f(x)')
title('Funcion Escalon Demostracion del Fenomeno de Gibs')