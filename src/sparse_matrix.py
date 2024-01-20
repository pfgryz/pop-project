from typing import TypeVar, List, Tuple

SparseMatrixPosition = int
SparseMatrixElement = TypeVar("SparseMatrixElement")
SparseMatrix = List[Tuple[SparseMatrixPosition, SparseMatrixElement]]


class SparseMatrixHelpers:

    @staticmethod
    def add(matrix: SparseMatrix[SparseMatrixElement],
            value: SparseMatrixElement) -> SparseMatrix[SparseMatrixElement]:
        """
        Adds element to sparse matrix. Works on original object

        :param matrix: SparseMatrix
        :param value: Value to add
        :return: Same matrix
        """
        count = len(matrix)
        matrix.append((count, value))
        return matrix

    @staticmethod
    def remove(matrix: SparseMatrix[SparseMatrixElement], position: int) -> \
            SparseMatrix[SparseMatrixElement]:
        """
        Removes element from sparse matrix. Works on original object

        :param matrix: SparseMatrix
        :param position: Position
        :return: Same matrix
        """
        matrix.pop(position)

        count = len(matrix)
        for index in range(position, count):
            _, value = matrix[index]
            matrix[index] = (index, value)

        return matrix

    @staticmethod
    def validate(matrix: SparseMatrix[SparseMatrixElement]) -> bool:
        """
        Checks if sparse matrix is valid

        :param matrix: SparseMatrix
        :return: Is matrix valid
        """
        count = len(matrix)
        for index in range(count):
            position, _ = matrix[index]

            if position != index:
                return False

        return True

    @staticmethod
    def sort(matrix: SparseMatrix[SparseMatrixElement]) -> \
            SparseMatrix[SparseMatrixElement]:
        """
        Sorts sparse matrix. Works on original object

        :param matrix: Matrix to sort
        :return: Same matrix
        """
        matrix.sort(key=lambda item: item[0])
        return matrix
