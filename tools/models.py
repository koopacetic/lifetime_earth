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


YEAR_HOURS = 365.2422 * 24  # tropical year in hours; Earth's orbit held fixed (farhat2022, Table D.3)


def year_from_day_length(t: int):
    """Solar days per year = YEAR_HOURS / day length (h), with day length from data/series/day_length.json.
    Blank wherever day length is blank."""
    from common import load_series, series_value
    day = next(s for s in load_series() if s["id"] == "day_length")
    r = series_value(day, t)
    return None if r is None else YEAR_HOURS / r[0]


MODELS = {"gough1981": gough1981, "year_from_day_length": year_from_day_length}
