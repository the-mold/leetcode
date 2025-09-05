class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        self.reflection(image)
        self.invert(image)
        return image

    def reflection(self, image):
        n = len(image)
        for i in range(n):
            for j in range(n // 2):
                image[i][j], image[i][-j-1] = image[i][-j-1], image[i][j] # In Python get the oposite array entry: image[i][~j] == image[i][-j-1]

    def invert(self, image):
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

# T:O(N)
# S:O(1)
