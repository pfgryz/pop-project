from src.matrix import Matrix


def test_add_to_empty_sparse_matrix():
    matrix = Matrix([])
    matrix.add(3)

    assert len(matrix) == 1
    assert matrix[0][0] == 0
    assert matrix[0][1] == 3


def test_add_to_sparse_matrix():
    matrix = Matrix(["a", "b"])
    matrix.add("c")

    assert len(matrix) == 3
    assert matrix[1][1] == "b"
    assert matrix[2][1] == "c"


def test_remove_from_end_sparse_matrix():
    matrix = Matrix(["a", "b", "c"])
    matrix.remove(2)

    assert len(matrix) == 2
    assert matrix[1][1] == "b"


def test_remove_from_middle_sparse_matrix():
    matrix = Matrix(["a", "b", "c"])
    matrix.remove(1)

    assert len(matrix) == 2
    assert matrix[1][1] == "c"


def test_validate_good_sparse_matrix():
    matrix = Matrix(["a", "b", "c"])

    assert matrix.validate()


def test_validate_invalid_sparse_matrix():
    matrix = Matrix(["a", "b", "c"])
    matrix._content[1] = (2, "b")
    matrix._content[2] = (1, "c")

    assert not matrix.validate()


def test_sort_sparse_matrix():
    matrix = Matrix(["a", "b", "c"])
    matrix._content[1] = (2, "b")
    matrix._content[2] = (1, "c")

    assert matrix[1][1] == "b"
    assert not matrix.validate()

    matrix.sort()

    assert matrix[1][1] == "c"
    assert matrix.validate()
