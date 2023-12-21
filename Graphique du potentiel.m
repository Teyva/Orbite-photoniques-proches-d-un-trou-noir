r = linspace(1.5, 16, 1000);
alpha = 0.3;
M = 1;

V = potentiel(r, alpha, M);
[V_max, idx_max] = max(V);

plot(r, V)
hold on;

line([r(idx_max) max(r)], [V_max V_max], 'Color', 'k', 'LineStyle', '-')
line([r(idx_max) r(idx_max)], [0 V_max], 'Color', 'k', 'LineStyle', '-')

text(r(idx_max) + 0.6, 0.02, sprintf(' r = r_{ph}'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'top')
text(11.5, V_max + 0.01, sprintf(' b < b_{ph}'), 'HorizontalAlignment', 'right', 'VerticalAlignment', 'bottom')
text(11, V_max - 0.002, sprintf(' b = b_{ph}'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'top')
text(11, V_max - 0.01, sprintf(' b > b_{ph}'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'top')

hold off;

xlabel('r');
ylabel('V(r)');
xlim([1.5 16]);
ylim([0 0.06]);

function f = potentiel(r, alpha, M)
    f = (1 ./ r.^2) .* (1 + ((r.^2) / (2 * alpha)) .* (1 - sqrt(1 + ((8 * alpha * M) ./ (r.^3)))));
    f(f < 0) = NaN; 
end
