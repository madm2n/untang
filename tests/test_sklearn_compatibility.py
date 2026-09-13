from sklearn.utils.estimator_checks import parametrize_with_checks

from untang import Resovler


class TestSklearnCompatibility:
    @parametrize_with_checks([Resovler()])
    def test_estimator(self, estimator, check) -> None:
        check(estimator)
