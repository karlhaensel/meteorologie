# global const
R_l = 287.05  # J kg^-1 K^-1


# functions
def p(T: float | None = None,
      rho: float | None = None,
      p: float | None = None) -> float | ValueError:
    if T is None or rho is None:
        return ValueError("Error: T and rho must be given to calculate p.")
    if (
        (p is not None) and round(p, 0) != round(rho * R_l * T, 0)
    ):
        return ValueError("Error: Given p does not match calculated p.")
    return rho * R_l * T


def T(p: float | None = None,
      rho: float | None = None,
      T: float | None = None) -> float | ValueError:
    if p is None or rho is None:
        return ValueError("Error: p and rho must be given to calculate T.")
    if (
        (T is not None) and round(T, 0) != round(p / (rho * R_l), 0)
    ):
        return ValueError("Error: Given T does not match calculated T.")
    return p / (rho * R_l)


def rho(p: float | None = None,
        T: float | None = None,
        rho: float | None = None) -> float | ValueError:
    if p is None or T is None:
        return ValueError("Error: p and T must be given to calculate rho.")
    if (
        (rho is not None) and round(rho, 0) != round(p / (R_l * T), 0)
    ):
        return ValueError("Error: Given rho does not match calculated rho.")
    return p / (R_l * T)
