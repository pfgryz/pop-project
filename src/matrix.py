from typing import TypeVar, List, Tuple

MatrixPosition = int
MatrixElement = TypeVar("MatrixElement")
SparseMatrix = List[Tuple[MatrixPosition, MatrixElement]]


class MatrixHelpers:

    @staticmethod
    def add(matrix: SparseMatrix[MatrixElement],
            value: MatrixElement) -> SparseMatrix[MatrixElement]:
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
    def remove(matrix: SparseMatrix[MatrixElement], position: int) -> \
            SparseMatrix[MatrixElement]:
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
    def validate(matrix: SparseMatrix[MatrixElement]) -> bool:
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
    def sort(matrix: SparseMatrix[MatrixElement]) -> \
            SparseMatrix[MatrixElement]:
        """
        Sorts sparse matrix. Works on original object

        :param matrix: Matrix to sort
        :return: Same matrix
        """
        matrix.sort(key=lambda item: item[0])
        return matrix
