import numpy as np

#ベクトルを実現
class Vector:
    #コンストラクタ
    def __init__(self, x, y) -> None:
        #numpyの計算を使うための値(private)
        self.__num = np.array([0,0])
        self.x = x
        self.y = y
        
    @classmethod
    def get_by_polar(cls, mag, angle) -> "Vector":
        
        x = mag*np.cos(angle)
        y = mag*np.sin(angle)
        
        return Vector(x,y)
        
    #コピーコンストラクタ
    def __copy__(self) -> "Vector":
        return Vector(self.x, self.y)
    
    
    #セッター(xとyの変化を__numに反映)
    def __setattr__(self, __name: str, __value) -> None:
        super().__setattr__(__name, __value)
        if(__name == "x"):
            self.__num[0] = __value
        elif(__name == "y"):
            self.__num[1] = __value
    
    #加算オペレーター
    def __add__(self, other: "Vector") -> "Vector":
        n = self.__num + other.getNum()
        
        return Vector(n[0], n[1])
    
    #減算オペレーター
    def __sub__(self, other: "Vector") -> "Vector":
        n = self.__num - other.getNum()
        
        return Vector(n[0], n[1])
    
    #乗算オペレーター
    def __mul__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return Vector(self.x*other, self.y*other)
    
    #除算オペレーター
    def __truediv__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return self
        else:
            return Vector(self.x/other, self.y/other)
    
    #文字列化
    def __str__(self) -> str:
        return "[" + str(self.x) + ", " + str(self.y) + "]"
    
    #内部の値をnp.arrayとして返す
    def getNum(self) -> np.ndarray:
        return self.__num
    
    #内積
    def dot(self, other: "Vector") -> float:
        return np.dot(self.__num, other.getNum())
    
    #大きさ
    def mag(self) -> float:
        return np.linalg.norm(self.__num, ord=2)
    
    #角度(degreeで出る)
    def angle(self) -> float:
        if(self.mag() == 0):
            return 0
        
        if(self.y >= 0):
            return np.degrees(np.arccos(self.x/self.mag()))
        else:
            return np.degrees(2*np.pi - np.arccos(self.x/self.mag()))
    
    #正規化
    def normalize(self) -> "Vector":
        if self.mag() == 0:
            return Vector(0,0)
        return Vector(self.x/self.mag(), self.y/self.mag())
    
    def change2list(self) -> tuple[int,int]:
        return (self.x, self.y)
        
    
#デバック用
if __name__ == "__main__" :
    print("test")
    v = Vector(2,2)
    print(v)
    v2 = Vector(1,1)
    print(v.dot(v2))