function R = derive(r, b, alpha, M)
    R = (r.^2).*sqrt((1./(b.^2)-(1./(r.^2)).*(1+((r.^2)./(2.*alpha)).*(1-sqrt(1+((8.*alpha.*M)./r.^3))))));
end