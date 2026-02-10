def read_matrix(rows, cols):
    """
    Read a matrix of a given size from standard input.

    Parameters:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.

    Returns:
        list[list[float]]: Matrix represented as a list of rows.
    """
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(float, input().split())))
    return matrix


def read_size(prompt):
    """
    Read matrix size from input with validation.

    The user must enter exactly two numeric values:
    number of rows and number of columns.

    Parameters:
        prompt (str): Prompt message displayed to the user.

    Returns:
        tuple[int, int]: Number of rows and columns.
    """
    while True:
        parts = input(prompt).split()
        if len(parts) != 2:
            print("Please enter two numbers: rows and columns.")
            continue
        if not all(p.lstrip("-").replace(".", "", 1).isdigit() for p in parts):
            print("Size must be numeric.")
            continue
        return map(int, parts)


def print_matrix(matrix):
    """
    Print a matrix row by row.

    Parameters:
        matrix (list[list[float]]): Matrix to be printed.

    Returns:
        None
    """
    for row in matrix:
        print(*row)


def add_matrices(a, b):
    """
    Add two matrices if their dimensions are equal.

    Parameters:
        a (list[list[float]]): First matrix.
        b (list[list[float]]): Second matrix.

    Returns:
        list[list[float]] | None: Sum of matrices or None if sizes differ.
    """
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None

    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def multiply_by_constant(matrix, constant):
    """
    Multiply all elements of a matrix by a constant.

    Parameters:
        matrix (list[list[float]]): Input matrix.
        constant (float): Constant multiplier.

    Returns:
        list[list[float]]: Resulting matrix.
    """
    return [[element * constant for element in row] for row in matrix]


def multiply_matrices(a, b):
    """
    Multiply two matrices if their dimensions are compatible.

    Parameters:
        a (list[list[float]]): First matrix.
        b (list[list[float]]): Second matrix.

    Returns:
        list[list[float]] | None: Product matrix or None if multiplication
        cannot be performed.
    """
    if len(a[0]) != len(b):
        return None

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            value = 0
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
            row.append(value)
        result.append(row)
    return result


def transpose_main(matrix):
    """
    Transpose a matrix across the main diagonal.

    Parameters:
        matrix (list[list[float]]): Input matrix.

    Returns:
        list[list[float]]: Transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]


def transpose_side(matrix):
    """
    Transpose a matrix across the side diagonal.

    Parameters:
        matrix (list[list[float]]): Input matrix.

    Returns:
        list[list[float]]: Transposed matrix.
    """
    return [
        [matrix[-j - 1][-i - 1] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def transpose_vertical(matrix):
    """
    Transpose a matrix across the vertical line.

    Parameters:
        matrix (list[list[float]]): Input matrix.

    Returns:
        list[list[float]]: Transposed matrix.
    """
    return [row[::-1] for row in matrix]


def transpose_horizontal(matrix):
    """
    Transpose a matrix across the horizontal line.

    Parameters:
        matrix (list[list[float]]): Input matrix.

    Returns:
        list[list[float]]: Transposed matrix.
    """
    return matrix[::-1]


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Parameters:
        matrix (list[list[float]]): Square matrix.

    Returns:
        float: Determinant value.
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        minor = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def inverse_matrix(matrix):
    """
    Calculate the inverse of a square matrix if it exists.

    Parameters:
        matrix (list[list[float]]): Square matrix.

    Returns:
        list[list[float]] | None: Inverse matrix or None if determinant is zero.
    """
    det = determinant(matrix)
    if det == 0:
        return None

    size = len(matrix)

    if size == 1:
        return [[1 / det]]

    cofactors = []
    for i in range(size):
        cofactor_row = []
        for j in range(size):
            minor = [
                row[:j] + row[j + 1:]
                for idx, row in enumerate(matrix) if idx != i
            ]
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = transpose_main(cofactors)
    return multiply_by_constant(adjugate, 1 / det)


def main():
    """
    Run the matrix processor program.

    Displays a menu, reads user input, and performs selected
    matrix operations until the user exits the program.

    Returns:
        None
    """

    while True:
        print(
            "\n1. Add matrices\n"
            "2. Multiply matrix by a constant\n"
            "3. Multiply matrices\n"
            "4. Transpose matrix\n"
            "5. Calculate a determinant\n"
            "6. Inverse matrix\n"
            "0. Exit"
        )

        choice = input("Your choice: \n> ")

        if choice == "0":
            break

        if choice == "1":
            r1, c1 = read_size("Enter size of first matrix: \n> ")
            print("Enter first matrix:")
            a = read_matrix(r1, c1)

            r2, c2 = read_size("Enter size of first matrix: \n> ")
            print("Enter second matrix:")
            b = read_matrix(r2, c2)

            result = add_matrices(a, b)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print_matrix(result)

        elif choice == "2":
            r, c = read_size("Enter size of first matrix: \n> ")
            print("Enter matrix:")
            matrix = read_matrix(r, c)
            constant = float(input("Enter constant: \n> "))

            print("The result is:")
            print_matrix(multiply_by_constant(matrix, constant))

        elif choice == "3":
            r1, c1 = read_size("Enter size of first matrix: \n> ")
            print("Enter first matrix:")
            a = read_matrix(r1, c1)

            r2, c2 = read_size("Enter size of first matrix: \n> ")
            print("Enter second matrix:")
            b = read_matrix(r2, c2)

            result = multiply_matrices(a, b)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print_matrix(result)

        elif choice == "4":
            print(
                "1. Main diagonal\n"
                "2. Side diagonal\n"
                "3. Vertical line\n"
                "4. Horizontal line"
            )
            t = input("Your choice: \n> ")

            r, c = read_size("Enter size of first matrix: \n> ")
            print("Enter matrix:")
            matrix = read_matrix(r, c)

            if t == "1":
                result = transpose_main(matrix)
            elif t == "2":
                result = transpose_side(matrix)
            elif t == "3":
                result = transpose_vertical(matrix)
            elif t == "4":
                result = transpose_horizontal(matrix)
            else:
                continue

            print("The result is:")
            print_matrix(result)

        elif choice == "5":
            r, c = read_size("Enter size of first matrix: \n> ")
            print("Enter matrix:")
            matrix = read_matrix(r, c)

            if r != c:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print(determinant(matrix))

        elif choice == "6":
            r, c = read_size("Enter size of first matrix: \n> ")
            print("Enter matrix:")
            matrix = read_matrix(r, c)

            result = inverse_matrix(matrix)
            if result is None:
                print("This matrix doesn't have an inverse.")
            else:
                print("The result is:")
                print_matrix(result)

if __name__ == "__main__":
    main()
