class SpiralMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def generate_spiral(self):
        # Starting values for the boundaries
        top, bottom, left, right = 0, self.size - 1, 0, self.size - 1
        current_number = 0

        while top <= bottom and left <= right:
            # Fill the top row from left to right
            for i in range(left, right + 1):
                self.matrix[top][i] = f"{current_number:02}"
                current_number += 1
            top += 1

            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                self.matrix[i][right] = f"{current_number:02}"
                current_number += 1
            right -= 1

            # Fill the bottom row from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    self.matrix[bottom][i] = f"{current_number:02}"
                    current_number += 1
                bottom -= 1

            # Fill the left column from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    self.matrix[i][left] = f"{current_number:02}"
                    current_number += 1
                left += 1

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(row))

def get_matrix_size():
    while True:
        try:
            size = int(input("Enter the size of the square matrix (positive integer): "))
            if size <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            return size
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    size = get_matrix_size()
    spiral_matrix = SpiralMatrix(size)
    spiral_matrix.generate_spiral()
    spiral_matrix.print_matrix()
