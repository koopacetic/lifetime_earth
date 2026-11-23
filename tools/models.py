"""Named analytic models for footer series (data/series/*.json with "model": "<name>").

Each model maps a year t (negative = past) to a value, or None where it isn't valid.
The series file carries the citation; keep formulas here and documented.
"""

SUN_AGE_NOW = 4.57e9  # years, as used by Gough (1981)


def gough1981(t: int):
    """Solar luminosity as % of present (Gough 1981, Solar Physics 74:21)."""
    age = SUN_AGE_NOW + t
    if age <= 0:
        return None
    return 100.0 / (1 + 0.4 * (1 - age / SUN_AGE_NOW))


MODELS = {"gough1981": gough1981}
