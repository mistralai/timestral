from importlib.metadata import distribution

import timestral


def test_private_distribution_preserves_timestral_import() -> None:
    installed_distribution = distribution("timestral-private")

    assert installed_distribution.read_text("top_level.txt") == "timestral\n"
    assert timestral.TimestralForecaster.__module__ == "timestral.forecaster"
