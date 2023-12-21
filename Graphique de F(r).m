r_values = linspace(0.1, 5, 1000);
M_values = 1;
alpha_values = zeros(4, 1);

for i = 1:4
    if 0 + i*0.2 == 0
        alpha_values(i) = 0.1;
    else
        alpha_values(i) = 0 + i*0.2;
    end
end
for j = 1:1
    M = M_values(j);
    for i = 1:4
        alpha = alpha_values(i);
        y = force(r_values, alpha, M);     
        plot(r_values, y, 'DisplayName', ['alpha = ', num2str(alpha)]);
        hold on;
    end
end

xlabel('r');
ylabel('f(r)');
legend('show','Location','southeast');

function f = force(r, alpha, M)
    f = real(1 + ((r.^2) ./ (2 .* alpha)) .* (1 - sqrt(1 + ((8 .* alpha .* M) ./ (r.^3)))));
end
