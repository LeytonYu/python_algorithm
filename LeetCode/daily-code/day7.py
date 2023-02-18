class Solution:
    def largest1BorderedSquare(self, grid):
        sum_row = []
        sum_col = []
        row_len = 0
        col_len = 0
        for row in grid:
            row_len += 1
            tp = 0
            tpl = [0]
            for j in row:
                tp += j
                tpl.append(tp)
            sum_row.append(tpl)
        for col in zip(*grid):
            col_len += 1
            tp = 0
            tpl = [0]
            for j in col:
                tp += j
                tpl.append(tp)
            sum_col.append(tpl)

        max_bc = min(row_len, col_len)
        for bc in range(max_bc, 0, -1):
            for i in range(row_len - bc + 1):
                for j in range(col_len - bc + 1):
                    if sum_col[j][i + bc] - sum_col[j][i] == bc\
                            and sum_col[j + bc - 1][i + bc] - sum_col[j + bc - 1][i] == bc\
                            and sum_row[i][j + bc] - sum_row[i][j] == bc\
                            and sum_row[i + bc - 1][j + bc] - sum_row[i + bc - 1][j] == bc:
                        return bc * bc
        return 0


if __name__ == '__main__':
    grid = [[1,1,1],[1,0,1],[1,1,1], [1,1,1]]
    print(Solution().largest1BorderedSquare(grid))

