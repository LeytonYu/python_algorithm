from typing import List


class Solution:
    """
    开氏度 = 摄氏度 + 273.15
    华氏度 = 摄氏度 * 1.80 + 32.00
    """
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        h = celsius * 1.8 + 32
        return [k, h]


if __name__ == '__main__':
    print(Solution().convertTemperature(122.11))