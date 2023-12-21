M = 1; % Valeur fixe de M
alpha_values = linspace(-8, 1, 100); % Créez un vecteur d'alpha
r_solutions = zeros(size(alpha_values)); % Initialisez un tableau pour les solutions r

for i = 1:length(alpha_values)
    alpha = alpha_values(i);
    equation_to_solve = @(r) fonctionisco(r, alpha, M) - r;
    
    % Fournissez une estimation initiale pour r
    % Assurez-vous que l'estimation initiale n'est pas égale à zéro
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
