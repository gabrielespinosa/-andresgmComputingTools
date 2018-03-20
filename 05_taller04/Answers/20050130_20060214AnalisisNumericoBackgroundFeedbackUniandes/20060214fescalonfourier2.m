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
        if mod(k,2)==0
            termino(k)=0;
        else
            termino(k)=sin(k*x(i));%hallar cada termino
        end
    end
    f(i)=sum(termino);%hallar f(x(i)) sumando los terminos ecuacion determinado por el modelo de fourier
end

%Graficas
plot(x,fn,'b',x,f,'r')

grid on
axis square
axis ([-pi pi -1 1])
legend('funcion normal','funcion aproximada por Fourier')
xlabel('x')
ylabel('f(x)')
title('Funcion Escalon Demostracion del Fenomeno de Gibs')