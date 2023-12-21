M = 1; 
alpha_values = linspace(-8, 1, 100); 
r_solutions = zeros(size(alpha_values)); 

for i = 1:length(alpha_values)
    alpha = alpha_values(i);
    equation_to_solve = @(r) fonctionisco(r, alpha, M) - r;

    r_initial_guess = 7; % Choisissez une valeur non nulle

    try
        r_solutions(i) = fzero(equation_to_solve, r_initial_guess);
    catch
        r_solutions(i) = NaN; % Si fzero échoue, assignez NaN ou une autre valeur par défaut
    end
end

plot(alpha_values, r_solutions, '-');
xlabel('\alpha');
ylabel('r_{isco}');
grid on;
