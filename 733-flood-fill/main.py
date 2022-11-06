class Solution:
    def updateImage(self, image, pt, act, color):
        image_pt = image[pt[0]][pt[1]]
        if image_pt == act and image_pt != color:
            image = self.floodFill(image, pt[0], pt[1], color)
        return image


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        srsize = len(image) - 1
        scsize = len(image[0]) - 1
        
        srp = sr + 1 if sr < srsize else sr
        srm = sr - 1 if sr > 0 else sr

        scp = sc + 1 if sc < scsize else sc
        scm = sc - 1 if sc > 0 else sc

        act = image[sr][sc]
        if act != color:
            image[sr][sc] = color

        pt1 = (sr, scp)
        pt2 = (sr, scm)
        pt3 = (srp, sc)
        pt4 = (srm, sc)

        image = self.updateImage(image, pt1, act, color)
        image = self.updateImage(image, pt2, act, color)
        image = self.updateImage(image, pt3, act, color)
        image = self.updateImage(image, pt4, act, color)

        return image
