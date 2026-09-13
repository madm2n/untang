"""Scikit-learn compatible estimators."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.linear_model import LogisticRegression
from sklearn.utils.validation import check_array, check_is_fitted, check_X_y


class Resovler(ClassifierMixin, BaseEstimator):
    """Scikit-learn compatible entity-resolution estimator scaffold.

    Until entity-resolution logic is implemented, the estimator delegates to
    logistic regression while establishing the public estimator contract.
    """

    def fit(self, X: ArrayLike, y: ArrayLike) -> Resovler:
        """Fit the resolver on candidate pairs and match labels."""
        input_columns = getattr(X, "columns", None)
        X_valid, y_valid = check_X_y(X, y, accept_sparse=False)

        self._model = LogisticRegression(max_iter=1000)
        self._model.fit(X_valid, y_valid)
        self.classes_ = self._model.classes_
        self.n_features_in_ = X_valid.shape[1]

        if input_columns is not None and all(
            isinstance(column, str) for column in input_columns
        ):
            self.feature_names_in_ = np.asarray(input_columns, dtype=object)

        return self

    def predict(self, X: ArrayLike) -> np.ndarray:
        """Predict the match label for each candidate pair."""
        check_is_fitted(self, "_model")
        return np.asarray(self._model.predict(check_array(X, accept_sparse=False)))

    def predict_proba(self, X: ArrayLike) -> np.ndarray:
        """Return class probabilities for each candidate pair."""
        check_is_fitted(self, "_model")
        return np.asarray(
            self._model.predict_proba(check_array(X, accept_sparse=False))
        )
