import pandas as pd

from untang import Resovler, __version__


class TestPackage:
    def test_version_is_defined(self) -> None:
        assert __version__ == "0.1.0"

    def test_resovler_has_classifier_api(self) -> None:
        X = pd.DataFrame(
            {
                "name_similarity": [0.1, 0.2, 0.8, 0.9],
                "address_similarity": [0.2, 0.1, 0.7, 0.95],
            }
        )
        y = pd.Series([False, False, True, True])
        resolver = Resovler().fit(X, y)

        assert resolver.predict(X).shape == (4,)
        assert resolver.predict_proba(X).shape == (4, 2)
        assert resolver.classes_.tolist() == [False, True]
        assert resolver.n_features_in_ == 2
        assert resolver.feature_names_in_.tolist() == [
            "name_similarity",
            "address_similarity",
        ]
