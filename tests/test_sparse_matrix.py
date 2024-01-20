from src.sparse_matrix import SparseMatrix, SparseMatrixHelpers


def test_add_to_empty_sparse_matrix():
    matrix: SparseMatrix[int] = []

    SparseMatrixHelpers.add(matrix, 3)

    assert len(matrix) == 1
    assert matrix[0][0] == 0
    assert matrix[0][1] == 3


def test_add_to_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (1, "b")]

    SparseMatrixHelpers.add(matrix, "c")

    assert len(matrix) == 3
    assert matrix[1][1] == "b"
    assert matrix[2][1] == "c"


def test_remove_from_end_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (1, "b"), (2, "c")]

    SparseMatrixHelpers.remove(matrix, 2)

    assert len(matrix) == 2
    assert matrix[1][1] == "b"


def test_remove_from_middle_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (1, "b"), (2, "c")]

    SparseMatrixHelpers.remove(matrix, 1)

    assert len(matrix) == 2
    assert matrix[1][1] == "c"


def test_validate_good_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (1, "b"), (2, "c")]

    assert SparseMatrixHelpers.validate(matrix)


def test_validate_invalid_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (2, "b"), (1, "c")]

    assert not SparseMatrixHelpers.validate(matrix)


def test_sort_sparse_matrix():
    matrix: SparseMatrix[str] = [(0, "a"), (2, "b"), (1, "c")]

    assert matrix[1][1] == "b"
    assert not SparseMatrixHelpers.validate(matrix)

    SparseMatrixHelpers.sort(matrix)

    assert matrix[1][1] == "c"
    assert SparseMatrixHelpers.validate(matrix)
