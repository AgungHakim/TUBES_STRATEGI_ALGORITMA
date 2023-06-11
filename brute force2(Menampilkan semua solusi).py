#Kompleksitas Waktu : O(n^2 * n!), di mana n adalah ukuran papan.
#Kompleksitas Ruang : O(n^2 )
import time
def is_safe(board, row, col, N):
    # Periksa baris yang sama di kolom sebelumnya
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Periksa diagonal atas kiri
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Periksa diagonal bawah kiri
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens_util(board, col, N, solutions):
    # Basis: Jika semua kolom telah diperiksa
    if col >= N:
        solution = []
        for row in board:
            solution.append(' '.join(['Q' if cell == 1 else '.' for cell in row]))
        solutions.append(solution)
        return

    # Iterasi melalui setiap baris dalam kolom saat ini
    for i in range(N):
        if is_safe(board, i, col, N):
            # Tempatkan ratu pada posisi ini
            board[i][col] = 1

            # Coba untuk menempatkan ratu di kolom berikutnya
            solve_n_queens_util(board, col + 1, N, solutions)

            # Hapus ratu dari posisi ini untuk mencoba kemungkinan lain
            board[i][col] = 0


def solve_n_queens(N):
    a = 0
    # Inisialisasi papan catur
    board = [[0] * N for _ in range(N)]

    # Simpan semua solusi dalam list of lists
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    # Tampilkan semua solusi
    for solution in solutions:
        a = a + 1
        for row in solution:
            print(row)
        print()
    print("Jumlah Kemungkinan: ",a, "posisi")
    

# Masukan input 
start = time.time()
N = int(input("Masukkan jumlah N : "))
#N = 7
solve_n_queens(N)

end = time.time()
print("Waktu eksekusi:", end - start)
