function f = force(r, alpha, M)
    f = real(1 + ((r.^2) ./ (2 .* alpha)) .* (1 - sqrt(1 + ((8 .* alpha .* M) ./ (r.^3)))));
end
